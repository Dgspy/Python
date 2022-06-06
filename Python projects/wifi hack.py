import subprocess
a = subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8').split('\n')
a = [i.split("i")[1][1:-1] for i in a if "all user profile " in i]
for i in a:
    result = subprocess.check_output(
    ['netsh','wlan','show','profile',i,'key=clear'])
    result = [b.split(":")[1][1:-1] for b in result if "key content" in b]
    try:
        print("{:<30}| {:<}".format(i,result[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, " p"))