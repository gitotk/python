import re

ptr = ["Apple", "Google", "Thank you"]
str = ["Hello", "Google", "Thank you"]

for vptr in ptr:
    print("-----------")
    pattern = re.compile(vptr)

    for vstr in str:
        res = pattern.search(vstr)
        if res is not None:
            m = "○"
        else:
            m = "×"
        msg = "パターン：" + vptr + "　文字列：" + vstr + "　マッチ：" + m
        print(msg)
