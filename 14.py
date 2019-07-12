sale = {"東京":11, "大阪":22, "札幌":33, "名古屋":44}
print("現在のデータは",sale,"です")

k = input("追加キーを入力してください：")

if k in sale: 
    print(k, "のデータはすでに存在しています")
else:
    d = int(input("追加データを入力してください："))
    sale[k] = d
    print(k, "のデータとして", sale[k],"を追加しました")
print("現在のデータは",sale,"です")

k = input("どのキーのデータを変更？")

if k in sale:
    print(k, "のでーたは", sale[k],"です")
    
    d = int(input("データを入力してください："))
    sale[k] = d
    print(k, "のデータは", sale[k],"に変更されました")
else:
    print(k,"のデータはみつかりませんでした")
print("現在のデータは",sale,"です")

k = input("どのキーデータを削除しますか：")
if k in sale:
    print(k, "のでーたは", sale[k],"です")
    del sale[k]
    print("データを削除しました")
else:
    print(k, "のデータはみつかりません")
print("現在のデータは",sale,"です")


    
