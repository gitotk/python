import myclass as my
        
pr = my.Customer("鈴木", 55, "aaa@aaa.aaa", "0123-45-6789")

name = pr.getName()
age = pr.getAge()
address = pr.getAdr()
tel = pr.getTel()

print(name, "さんは", age, "歳です")
print("アドレスは", address, "電話番号は", tel)

