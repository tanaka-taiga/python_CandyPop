import sys

args = sys.argv

sheeps = args[1]
sheeps = int(sheeps)

for i in range(sheeps):
    #ファイルを開く
    sheep_file = open("../../files/sheep.txt", mode="w", encoding="utf-8")

    #ファイルに書き込む
    sheep_file.write("ひつじが"+ str(i+1) +"匹")

    #ファイルを閉じる
    sheep_file.close()
