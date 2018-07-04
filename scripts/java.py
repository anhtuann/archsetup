from scripts import tools

#INSTALL
packages = ['jdk10-openjdk',
            'jre10-openjdk-headless',
            'jdk9-openjdk',
            'jre9-openjdk-headless']
tools.pacaur(packages)

#CONFIGURATION
#tools.stow('package_name')
