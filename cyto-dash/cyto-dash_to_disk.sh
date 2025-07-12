#!/bin/bash
echo "Copying dash-cytoscape packages"
scp -r /srv/pypi/web/simple/dash-cytoscape/ ~/pypi/web/
scp -r /srv/pypi/web/packages/a9/80/482ec26e0da7b54befb2122f8bdb423cd035c5942e642259cbaad284da80/ ~/pypi/packages
scp -r /srv/pypi/web/packages/52/c2/4b26c5eb7b75b5513c75c91cad36b42ce4cbb580cbdf3df926a304561bf1/ ~/pypi/packages
scp -r /srv/pypi/web/packages/3d/c3/fde252cdd33276a814ade3255b2df2268455b21bcbdeeea9488c42e46b87/ ~/pypi/packages
scp -r /srv/pypi/web/packages/94/33/0dc4d0d0b50f07c6c7be0b76d801d12e56eee167bd81a4bdb1290e0a656a/ ~/pypi/packages
scp -r /srv/pypi/web/packages/aa/93/d9db22331dcad4a055631372816bf4544a1a1a852fb2fa3a2905c6682198/ ~/pypi/packages
scp -r /srv/pypi/web/packages/a1/98/93b356b47aca71d4fb1065990137b6b75eb527e8d1cd0e87dc037cead113/ ~/pypi/packages
scp -r /srv/pypi/web/packages/34/be/21ee645cb7943ab71b08e32c90c26c71d3d03f08e5a52c50e6e76568f0a0/ ~/pypi/packages
scp -r /srv/pypi/web/packages/47/45/dd3752058d5a7f853c17d7b292db1311be884e32e4d90bbbebf3b4944e05/ ~/pypi/packages
scp -r /srv/pypi/web/packages/20/b3/f65ebbe40bc105d89ed0c828bae8e782839a5562d4aa8ee55b41b02cd7f2/ ~/pypi/packages
scp -r /srv/pypi/web/packages/33/2d/298a3d89ce664f0af214569281ccc933c0cc3b797705b079bc12c8b2b623/ ~/pypi/packages
scp -r /srv/pypi/web/packages/2a/0a/9c596c852da3692023a209164fd6e396b0d72923a81c2ace1f5e375a5ebd/ ~/pypi/packages
scp -r /srv/pypi/web/packages/ea/b7/0d511af853024241dc3192bea77e4753ea606187bd2dd777a8209a5b01bb/ ~/pypi/packages
echo "Copying pypi packages complete."
exit
