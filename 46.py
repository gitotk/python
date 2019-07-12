import datetime

dt = datetime.datetime.now()

dt_plus = dt + datetime.timedelta(days=1)

print("今日は　", dt, "です")
print("１日後は", dt_plus, "です")

dt_minus = dt - datetime.timedelta(days=1)

print("１日前は", dt_minus, "です")
