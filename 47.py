import datetime

dt = datetime.datetime.now()

str = dt.strftime("%c")

dt_plus = dt + datetime.timedelta(days=1)
str_plus = dt_plus.strftime("%Y/%m/%d")

print("現在は　", str, "です")
print("１日後は", str_plus, "です")

dt_minus = dt - datetime.timedelta(days=1)
str_minus = dt_minus.strftime("%Y/%m/%d")

print("１日前は", str_minus, "です")
