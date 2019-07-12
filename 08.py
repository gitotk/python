city = ["東京","大阪","札幌","京都"]
sale = [80,90,40,20,32,89]

print("city:",city)
print("sale:",sale)

for d in zip(city,sale):
    print(d)

print("データとインデックスの組み合わせ")

for d in enumerate(city):
    print(d)


print("データ分解")

for c,s in zip(city,sale):
    print("都市は",c, "売上は",s)

c1,c2,c3,c4 = city
print("ここは",c3)

