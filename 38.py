import re

ptr = "\.(csv|html|py)$"
str = ["Sample.csv", "Sample.exe", "test.py", "index.html"]

print("csv、html、py拡張子をtxtに変換します")

pattern = re.compile(ptr)
for vstr in str:
    res = pattern.sub(".txt", vstr)
    msg = "(変換前)" + vstr + "(変換後)" + res
    print(msg)
    
