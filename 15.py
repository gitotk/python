sale = {"東京":11, "大阪":22, "札幌":33, "名古屋":44}
print("現在のデータは",sale,"です")

print("キーを表示します")
for k in sale.keys():
    print(k, end="\t")
print()

print("値を表示します")
for v in sale.values():
    print(v, end="\t")
print()

print("キーと値を表示します")
for i in sale.items():
    print(i, end="")
print()



