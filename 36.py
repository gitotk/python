str = input("文字列入力：")
key = input("検索文字列：")

res = str.find(key)

if res != -1:
    print(str, "の", res, "の位置に", key, "がみつかりました")
else:
    print(str, "の中に", key, "がみつかりません")
