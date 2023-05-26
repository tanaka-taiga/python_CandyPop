import sys
import qrcode
import os

args = sys.argv

txtpass = args[1]

with open(txtpass, encoding="utf-8") as urltxt:

    for i, line in enumerate(urltxt):
        img = qrcode.make(line)
        path = os.path.abspath("/home/matcha-23training/Python/Python_git/files/"+ str(i+1) +".png")
        img.save(path)


