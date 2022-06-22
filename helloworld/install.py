import os, stat, wget

def install():
    wget.download('https://raw.githubusercontent.com/repo/helloworld/dist/helloworld', '/tmp/')
    if not os.path.isdir('~/.bin/pypack'):
        print("PyPack has not been installed Correctly! please install it with ensure_pypack.")
        pass
    else:
        os.mkdir(os.path.expanduser("~/.bin/pypack/helloworld"))
    os.rename("/tmp/package", os.path.expanduser("~/.bin/pypack/helloworld/helloworld"))
    os.chmod(os.path.expanduser("~/.bin/pypack/helloworld/helloworld"), os.stat(os.path.expanduser("~/.bin/pypack/helloworld/helloworld")).st_mode | stat.S_IEXEC)
