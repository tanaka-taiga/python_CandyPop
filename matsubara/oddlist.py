import sys
args = sys.argv

list = ["Kurita","Tanaka","Kaneda","Noda","Koyama","Adachi","Kurayama","Ohyama","Kishida"]

outlist = []
for i in range(0,len(list)-1):
    if(i % 2 != 0):
        outlist.append(list[i])
    else:
        continue

print(outlist,end="")
