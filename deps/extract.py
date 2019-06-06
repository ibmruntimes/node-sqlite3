import sys
import tarfile
import os
import platform

tarball = os.path.abspath(sys.argv[1])
dirname = os.path.abspath(sys.argv[2])
tfile = tarfile.open(tarball, 'r:gz')
tfile.extractall(dirname)
if platform.system() == 'OS/390':
  os.system("chtag -R -tc 819 %s" % dirname)
sys.exit(0)
