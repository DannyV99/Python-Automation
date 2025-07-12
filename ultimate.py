#!/usr/bin/env python3
# Shebang line ensuring the script is run with the user's default Python 3 interpreter.

import sys, re  # sys for CLI args & exiting; re for regex utilities.
from bs4 import BeautifulSoup  # HTML parser for scraping anchor tags.

# --- Helper functions ------------------------------------------------------- #

def normalize(name: str) -> str:
    """Return a 'normalized' package/file name (lowercase, no dashes/underscores)."""
    # Strip whitespace, make lowercase, remove '-' and '_' for consistent matching.
    return re.sub(r"[-_]", "", name.strip().lower())


def generate(pkg, direction, html_file, out):
    """Core routine to build a copy script for <pkg> in the chosen <direction>."""
    want = normalize(pkg)  # Normalized package name we're searching for.

    # Attempt to read & parse the specified HTML index file.
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
    except Exception as e:
        # If file can't be read, abort the script with an error message.
        sys.exit(f"❌ cannot read {html_file}: {e}")

    scp, hashes = [], set()  # scp = list of commands; hashes = unique file dirs.

    # Build the first scp command for the simple/ directory, direction‑dependent.
    if direction == "send":
        scp.append(f'scp -r ~/pypi/web/{pkg}/ /srv/pypi/web/simple/')
    else:
        scp.append(f'scp -r /srv/pypi/web/simple/{pkg}/ ~/pypi/web/')

    # Loop over every <a href="…"> element in the index to gather package files.
    for a in soup.find_all("a", href=True):
        href = a["href"]  # Extract href attribute value.
        if "../../packages/" not in href:
            continue  # Skip non‑package links.
        filename = href.split("/")[-1]  # Get filename portion at end of URL.
        if normalize(filename.split("-")[0]) != want:
            continue  # Skip if the filename isn't for the package we want.

        # Extract the nested hash directory structure: xx/yy/<hash>/file
        xx, yy, hsh = href.replace("../../packages/", "").split("/")[:3]
        if hsh in hashes:
            continue  # We've already handled this hash directory.
        hashes.add(hsh)  # Remember we've seen it.

        # Form src/dst paths for the package file tree depending on direction.
        if direction == "send":
            src = f"~/pypi/packages/{hsh}/"
            dst = f"/srv/pypi/web/packages/{xx}/{yy}/"
        else:
            src = f"/srv/pypi/web/packages/{xx}/{yy}/{hsh}/"
            dst = "~/pypi/packages"

        # Append the recursive scp command to copy this hash directory.
        scp.append(f"scp -r {src} {dst}")

    # Abort if no matching packages were discovered in the HTML index.
    if not hashes:
        sys.exit(f"❌ No links for package “{pkg}” in {html_file}")

    # Final informational echo commands.
    scp.append('echo "Copying pypi packages complete."')
    if direction == "send":
        scp.append('echo "Remember to edit /srv/pypi/web/index.html"')
    scp.append("exit")  # End of generated bash script.

    # Write the assembled bash script to <out>.
    try:
        with open(out, "w", encoding="utf-8") as f:
            f.write("#!/bin/bash\n")
            f.write(f'echo "Copying {pkg} packages"\n')
            f.write("\n".join(scp) + "\n")
        print(f"✅ Wrote {out} ({len(hashes)} hashes).")
    except Exception as e:
        sys.exit(f"❌ cannot write {out}: {e}")


# --- Main entry point ------------------------------------------------------- #

if __name__ == "__main__":
    # Expect at least 2 positional args: <package> and <send|receive>.
    if len(sys.argv) < 3:
        sys.exit("Usage: generate.py <package> <send|receive> [html] [out]")

    pkg  = sys.argv[1]                         # Package name to process.
    mode = sys.argv[2].lower()                 # Direction, case‑normalized.
    html = sys.argv[3] if len(sys.argv) > 3 else "index.html"  # HTML file path.
    out  = sys.argv[4] if len(sys.argv) > 4 else "copy_package.sh"  # Output shell script path.

    if mode not in ("send", "receive"):
        sys.exit("direction must be send or receive")  # Validate mode.

    generate(pkg, mode, html, out)  # Call main generator function.
