from scripts import tools

#INSTALL
packages = ['weechat']
tools.pacaur(packages)

#CONFIGURATION
tools.mkdir('~/.weechat/python/autoload')
with tools.cd('~/.weechat/python'):
    tools.bash_cmd("wget 'https://github.com/GermainZ/weechat-vimode/raw/master/vimode.py'")
    tools.link_conf('~/.weechat/python/vimode.py', '~/.weechat/python/autoload/vimode.py')
