from bs4 import BeautifulSoup

html_file = "index.html"
output_script = "copy_dash_cytoscape.sh"

with open(html_file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

seen = set()
scp_lines = []

for a in soup.find_all("a"):
    href = a.get("href", "")
    if "../../packages/" in href:
        parts = href.strip().split("/")
        # parts = ['..', '..', 'packages', 'XX', 'YY', '<HASH>', '<filename>']
        if len(parts) >= 7:
            xx = parts[3]
            yy = parts[4]
            full_hash = parts[5]

            if full_hash not in seen:
                seen.add(full_hash)
                src = f"~/pypi/packages/{full_hash}/"
                dest = f"/srv/pypi/web/packages/{xx}/{yy}/"
                scp_lines.append(f"scp -r  {src} {dest}")

script = [
    "#!/bin/bash",
    'echo "Copying dash-cytoscape packages"',
    "scp -r  ~/pypi/web/dash-cytoscape/ /srv/pypi/web/simple/"
]
script += scp_lines
script += [
    'echo "Copying pypi packages complete."',
    'echo "remember to edit the /srv/pypi/web/index.html and add the line for the new package"',
    "exit"
]

with open(output_script, "w") as f:
    f.write("\n".join(script))

print(f"✅ Shell script written to {output_script}")

