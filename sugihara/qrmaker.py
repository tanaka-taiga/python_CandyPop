import qrcode #パッケージのインポート
import os
import sys
args = sys.argv
input1 = str(args[1])
i=1

file = open(input1,mode="r",encoding="utf-8")
for line in file:
    path =  os.path.join(".","output",str(i)+".png")
    img = qrcode.make(line)
    img.save(path)
    i=i+1
