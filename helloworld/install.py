import os, stat

os.rename("dist", os.path.expanduser("~/.bin/pypack/helloworld"))
os.chmod(os.path.expanduser("~/.bin/pypack/helloworld/helloworld"), os.stat(os.path.expanduser("~/.bin/pypack/helloworld/helloworld")).st_mode | stat.S_IEXEC)
