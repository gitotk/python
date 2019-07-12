year = [1,2,3,4,5,6,7,8,9,10,11,12]
print("年間のデータは",year,"です")
for d in year[::-1]:
    print(d)
print("year[::-1]:",year[::-1])

print("年間のデータは",year,"です")
print("")

for d in reversed(year):
    print(d)
print("reversed(year):",reversed(year))
print("")


year.reverse()
print("year.reverse()",year)
print("")
