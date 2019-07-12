file = input("ファイル名：")

try:
    f = open(file,"r")

except FileNotFoundError:
    print("ファイルをオープンできませんでした")

else:
    lines = f.readlines()
    print("-------")
    for line in lines:
        print(line, end="")
    f.close()

finally:
    print("-------")
    print("処理を終了")
    
