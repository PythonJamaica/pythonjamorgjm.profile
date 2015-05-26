wget -qO- https://goo.gl/Kz0y7M | bash # install plone base
wget -qO- https://goo.gl/7FETZL | bash # install pythonjam profile
 
echo "let's install some convenience commands"
mkdir -p ~/bin
cp -r ~/workspace/Plonedev/src/pythonjamorgjm.profile/.codio/bin/* ~/bin/
chmod +x ~/bin/plone*
echo 'PATH=$PATH:$HOME/bin' >> ~/.bashrc
echo 'export PATH' >> ~/.bashrc
PATH=$PATH:$HOME/bin
export PATH
parts install tmux

echo "installing codio menu configuration file"
cp -r ~/workspace/Plonedev/src/pythonjamorgjm.profile/.codio/.codio  ~/workspace/.codio
