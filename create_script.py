import sys
import re
from scripts import tools

script_name = sys.argv[-1]
script_path = '~/Projects/archsetup/scripts/{}.py'.format(script_name)
tools.bash_cmd('touch {}'.format(script_path))

template = """
from scripts import tools

#INSTALL
packages = []
tools.pacaur(packages)

#CONFIGURATION
tools.stow('package_name')
"""

template = re.sub("^\s+|\s+$", "", template, flags=re.UNICODE)

tools.bash_cmd('echo "{}" > {}'.format(template, script_path))
print('{}.py successfully created'.format(script_name))
