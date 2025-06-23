#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup

def generate_script(package_name, direction, html_file="index.html", output_script="copy_package.sh"):
    package_name_underscore = package_name.replace("-", "_")

    try:
        with open(html_file, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        print(f"❌ HTML file '{html_file}' not found.")
        sys.exit(1)

    seen = set()
    scp_lines = []

    # Add line for the simple web directory (package folder)
    if direction == "send":
        scp_lines.append(f'scp -r ~/pypi/web/{package_name}/ /srv/pypi/web/simple/')
    else:
        scp_lines.append(f'scp -r /srv/pypi/web/simple/{package_name}/ ~/pypi/web/')

    # Extract package hashes and build scp commands
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "../../packages/" in href and package_name_underscore in href:
            # Remove the leading ../../
            clean_href = href.replace("../../packages/", "")
            parts = clean_href.strip().split("/")

            if len(parts) >= 4:
                xx, yy, full_hash = parts[0], parts[1], parts[2]

                if full_hash not in seen:
                    seen.add(full_hash)

                    if direction == "send":
                        src = f"~/pypi/packages/{full_hash}/"
                        dest = f"/srv/pypi/web/packages/{xx}/{yy}/"
                    else:
                        src = f"/srv/pypi/web/packages/{xx}/{yy}/{full_hash}/"
                        dest = "~/pypi/packages"

                    scp_lines.append(f"scp -r {src} {dest}")

    if not seen:
        print(f"❌ No packages found for '{package_name}' in {html_file}")
        sys.exit(1)

    # Add footer
    scp_lines.append('echo "Copying pypi packages complete."')
    if direction == "send":
        scp_lines.append('echo "Remember to edit the /srv/pypi/web/index.html and add the line for the new package"')

    scp_lines.append("exit")

    # Write script file
    with open(output_script, "w") as f:
        f.write("#!/bin/bash\n")
        f.write(f'echo "Copying {package_name} packages"\n')
        for line in scp_lines:
            f.write(line + "\n")

    print(f"✅ Script generated in '{output_script}' for package '{package_name}' with direction '{direction}'")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_script.py <package_name> <send|receive> [html_file] [output_script]")
        print("Example: python3 generate_script.py dash-cytoscape send index.html copy_send.sh")
        sys.exit(1)

    package_name = sys.argv[1]
    direction = sys.argv[2].lower()
    html_file = sys.argv[3] if len(sys.argv) > 3 else "index.html"
    output_script = sys.argv[4] if len(sys.argv) > 4 else "copy_package.sh"

    if direction not in ("send", "receive"):
        print("Direction must be 'send' or 'receive'")
        sys.exit(1)

    generate_script(package_name, direction, html_file, output_script)

if __name__ == "__main__":
    main()
