import os
def ls():
    result = os.popen('ls -l').read()
    print(result)
    return
