#!/bin/bash
echo "Copying dash-cytoscape packages"
scp -r  ~/pypi/web/dash-cytoscape/ /srv/pypi/web/simple/
scp -r ~/pypi/packages/482ec26e0da7b54befb2122f8bdb423cd035c5942e642259cbaad284da80/ /srv/pypi/web/packages/a9/80/
scp -r  ~/pypi/packages/4b26c5eb7b75b5513c75c91cad36b42ce4cbb580cbdf3df926a304561bf1/ /srv/pypi/web/packages/52/c2/
scp -r  ~/pypi/packages/fde252cdd33276a814ade3255b2df2268455b21bcbdeeea9488c42e46b87/ /srv/pypi/web/packages/3d/c3/
scp -r  ~/pypi/packages/0dc4d0d0b50f07c6c7be0b76d801d12e56eee167bd81a4bdb1290e0a656a/ /srv/pypi/web/packages/94/33/
scp -r  ~/pypi/packages/d9db22331dcad4a055631372816bf4544a1a1a852fb2fa3a2905c6682198/ /srv/pypi/web/packages/aa/93/
scp -r  ~/pypi/packages/93b356b47aca71d4fb1065990137b6b75eb527e8d1cd0e87dc037cead113/ /srv/pypi/web/packages/a1/98/
scp -r  ~/pypi/packages/21ee645cb7943ab71b08e32c90c26c71d3d03f08e5a52c50e6e76568f0a0/ /srv/pypi/web/packages/34/be/
scp -r  ~/pypi/packages/dd3752058d5a7f853c17d7b292db1311be884e32e4d90bbbebf3b4944e05/ /srv/pypi/web/packages/47/45/
scp -r  ~/pypi/packages/f65ebbe40bc105d89ed0c828bae8e782839a5562d4aa8ee55b41b02cd7f2/ /srv/pypi/web/packages/20/b3/
scp -r  ~/pypi/packages/298a3d89ce664f0af214569281ccc933c0cc3b797705b079bc12c8b2b623/ /srv/pypi/web/packages/33/2d/
scp -r  ~/pypi/packages/9c596c852da3692023a209164fd6e396b0d72923a81c2ace1f5e375a5ebd/ /srv/pypi/web/packages/2a/0a/
scp -r  ~/pypi/packages/0d511af853024241dc3192bea77e4753ea606187bd2dd777a8209a5b01bb/ /srv/pypi/web/packages/ea/b7/
echo "Copying pypi packages complete."
echo "remember to edit the /srv/pypi/web/index.html and add the line for the new package"
exit
