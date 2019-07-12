year = [1,2,3,4,5,6,7,8,9,10,11,12]

print("年間のデータは",year,"です")

data1 = year[0:6]
print("上期のデータは",data1,"です")

data2 = year[6:]
print("下期のデータは",data2,"です")

data3 = year[::2]
print("一ヶ月おきのデータは",data3,"です")

data4 = year[::-1]
print("逆順のデータは",data4,"です")

print("上半期のデータを差し替えます")
year[:6] = [0,0,0,0,0,0]
print("年間のデータは",year,"です")
