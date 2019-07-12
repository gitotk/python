sale = [80, 60, 22, 120, 70]

n = 1

print("リストの長さは", len(sale), "です")

for s in sale:
    print(n,":", s)
    n+=1

i = int(input("何番を変更？"))

print(i, "番のデータ", sale[i-1], "を変更します")

num = int(input("変更後のデータは？"))

sale[i-1] = num

print(i, "番のデータは", sale[i-1], "に変更されました")

for s in sale:
    print(n,":", s)
