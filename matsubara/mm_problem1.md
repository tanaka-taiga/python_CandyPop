# 問題
Googleでは、検索アルゴリズムにranking形式というものが用いられています。
ranking形式大量のビックデータから言葉と言葉の類似度を50次元のデータセットにし、それを辞書型データとして保存します。
そこから、類似度とはcos類似度という要素と要素の平面間距離の角度にてその要素の類似性を保証し、
ranking形式には、そのcos類似度が高い順に出力されるというシステムになっています。
が、今回は外部ビックデータをつかうと演習サーバーが壊れてしまうので、簡単なデータセットを準備します。

TABLE **word_xy**を準備して、A~Cの要素を任意に選び出す時、その要素とのコサイン類似度を
求めるプログラム(WordcosCalc.py)を作成しなさい
cos類似度(A,B)とcos類似度(A,C)、cos類似度(B,C)を求められればＯＫです。


A (v,w,x,y,z) = (1,3,2,3,1)
B (v,w,x,y,z) = (2,6,4,6,2)
C (v,w,x,y,z) = (1,3,4,2,1)

# 制約
mathモジュールを入れて行う事。
外部インポート抜きですべてここで行う事。
TABLEの要素は(name,v,w,x,y,z)で作り、nameはPRIMARY kEYとすること。