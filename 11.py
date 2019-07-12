data = [
    ["東京", 32,33],
    ["大阪", 91,32],
    ["札幌", 89,56]
    ]

print(data)

for dat in data:
    print("都市別データ:", dat)
    for d in dat:
        print(d, end="\t")
        print()

print(data[2][0], "の最高気温は", data[2][1], "最低気温は", data[2][2])
