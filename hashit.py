#!/usr/bin/python3

import subprocess
from sys import argv

argv=['hashit/hashit.py']
for x in argv:
    md5raw=subprocess.run(['md5sum',x],stdout=subprocess.PIPE)
    sh1raw= subprocess.run(['sha1sum',x],stdout=subprocess.PIPE)
    md5=md5raw.stdout.decode().split(' ')[0]
    sh1=sh1raw.stdout.decode().split(' ')[0]
    message='{:^40}\nmd5: {}\nsh1: {}'.format(x,md5,sh1)
    print(message)
