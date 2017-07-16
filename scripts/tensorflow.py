from scripts import tools

#INSTALL
packages = ['python-numpy',
            'python-wheel',
            'bazel']
tools.pacaur(packages)

#CONFIGURATION
tf_path = '~/Projects/tensorflow_build'
tf_version = 'r1.3'
tools.git_clone('https://github.com/tensorflow/tensorflow', tf_path)
with tools.cd(tf_path):
    tools.bash_cmd('git checkout {}'.format(tf_version), shell = True)
    tools.bash_cmd('./configure', shell = True)
    bazel_cmd = list()
    bazel_cmd.append('bazel')
    bazel_cmd.append('build')
    bazel_cmd.append('--config=opt')
    bazel_cmd.append('--copt=-mavx2')
    bazel_cmd.append('--copt=-mavx')
    bazel_cmd.append('--copt=-msse4.2')
    bazel_cmd.append('--copt=-msse4.1')
    bazel_cmd.append('--copt=-mfma')
    bazel_cmd.append('//tensorflow/tools/pip_package:build_pip_package')
    tools.bash_cmd(' '.join(bazel_cmd), shell = True)
    tools.bash_cmd('bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg', shell = True)
