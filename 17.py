city = {"東京", "大阪", "札幌", "名古屋"}
print(city)

d = input("追加データ：")
if d in city:
    print(d, "はすでに存在しています")
else:
    city.add(d)
    print(d,"を追加しました")
print("現在のデータは",city,"です")

d = input("削除するデータ：")
if d in city:
    city.remove(d)
    print(d,"を削除しました")
else:
    print(d,"はみつかりません")
print(city)






