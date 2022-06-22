import os, stat, requests

package = requests.get('https://raw.githubusercontent.com/repo/helloworld/dist/helloworld')
with open('/tmp/package', 'wb') as pack:
    pack.write(package.content)
    os.mkdir(os.path.expanduser("~/.bin/pypack/helloworld"))
    os.rename("/tmp/package", os.path.expanduser("~/.bin/pypack/helloworld/helloworld"))
os.chmod(os.path.expanduser("~/.bin/pypack/helloworld/helloworld"), os.stat(os.path.expanduser("~/.bin/pypack/helloworld/helloworld")).st_mode | stat.S_IEXEC)
