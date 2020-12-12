sed '/~f103207425\/\.local\/bin:$PATH/d' ~/.profile >> ~/.profile.new
mv ~/.profile.new ~/.profile
var1=''
grep 'alias oj="python2.7 ~/oj-cli/oj"' ~/.profile > var1
if [ '$var1' == 'alias oj="python2.7 ~/oj-cli/oj"' ]
then
	echo 'alias oj="python2.7 ~/oj-cli/oj"' >> .profile
fi
source ~/.profile
echo "Installed successfully! Please login first."
python2.7 oj login
