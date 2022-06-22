import os, stat, wget
from urllib.error import HTTPError

def install():
    try:
        wget.download('https://raw.githubusercontent.com/pypackman/repo/main/helloworld/dist/helloworld', '/tmp/')
    except HTTPError:
        print("download error. cleaning up.")
        try:
            os.remove('/tmp/install.py')
        except:
            exit()
    if os.path.isdir('~/.bin/pypack'):
        os.mkdir(os.path.expanduser("~/.bin/pypack/helloworld"))
    else:
        print("PyPack has not been installed Correctly! please install it with ensure_pypack.")
        exit()
    os.rename("/tmp/package", os.path.expanduser("~/.bin/pypack/helloworld/helloworld"))
    os.chmod(os.path.expanduser("~/.bin/pypack/helloworld/helloworld"), os.stat(os.path.expanduser("~/.bin/pypack/helloworld/helloworld")).st_mode | stat.S_IEXEC)
