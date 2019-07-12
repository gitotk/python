def append():
    print("データ追加")
def update():
    print("データ更新")
def delete():
    print("データ削除")

list = [append, update, delete]

res = int(input("操作番号を入力(0～2)："))

if 0 <= res and res < len(list):
    list[res]()
else:
    print("操作番号エラー")
    
