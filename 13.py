sale = {"東京":11, "大阪":22, "札幌":33, "名古屋":44}
print("現在のデータは",sale,"です")

k = input("どの支店？")

if k in sale:
    print(k, "のデータは", sale[k],"です")
else:
    print(k, "のデータは見つかりません")

    
