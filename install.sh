echo '[!] Updating...'
apt-get update > install.log
echo
echo '[!] Installing Dependencies...'
echo '    Python3'
apt-get -y install python3 &>> install.log
echo '    PHP'
apt-get -y install php &>> install.log
echo '    Requests'
pip install requests &>> install.log
echo
echo '[!] Installed.'
