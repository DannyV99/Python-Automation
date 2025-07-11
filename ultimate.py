#!/usr/bin/env python3
import sys, re
from bs4 import BeautifulSoup

def normalize(name: str) -> str:
    return re.sub(r"[-_]", "", name.strip().lower())

def generate(pkg, direction, html_file, out):
    want = normalize(pkg)
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
    except Exception as e:
        sys.exit(f"❌ cannot read {html_file}: {e}")

    scp, hashes = [], set()

    # simple/ directory
    if direction == "send":
        scp.append(f'scp -r ~/pypi/web/{pkg}/ /srv/pypi/web/simple/')
    else:
        scp.append(f'scp -r /srv/pypi/web/simple/{pkg}/ ~/pypi/web/')

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "../../packages/" not in href:
            continue
        filename = href.split("/")[-1]
        if normalize(filename.split("-")[0]) != want:
            continue

        xx, yy, hsh = href.replace("../../packages/", "").split("/")[:3]
        if hsh in hashes:
            continue
        hashes.add(hsh)

        if direction == "send":
            src = f"~/pypi/packages/{hsh}/"
            dst = f"/srv/pypi/web/packages/{xx}/{yy}/"
        else:
            src = f"/srv/pypi/web/packages/{xx}/{yy}/{hsh}/"
            dst = "~/pypi/packages"

        scp.append(f"scp -r {src} {dst}")

    if not hashes:
        sys.exit(f"❌ No links for package “{pkg}” in {html_file}")

    scp.append('echo "Copying pypi packages complete."')
    if direction == "send":
        scp.append('echo "Remember to edit /srv/pypi/web/index.html"')
    scp.append("exit")

    try:
        with open(out, "w", encoding="utf-8") as f:
            f.write("#!/bin/bash\n")
            f.write(f'echo "Copying {pkg} packages"\n')
            f.write("\n".join(scp) + "\n")
        print(f"✅ Wrote {out} ({len(hashes)} hashes).")
    except Exception as e:
        sys.exit(f"❌ cannot write {out}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: generate.py <package> <send|receive> [html] [out]")
    pkg  = sys.argv[1]
    mode = sys.argv[2].lower()
    html = sys.argv[3] if len(sys.argv) > 3 else "index.html"
    out  = sys.argv[4] if len(sys.argv) > 4 else "copy_package.sh"
    if mode not in ("send", "receive"):
        sys.exit("direction must be send or receive")
    generate(pkg, mode, html, out)
