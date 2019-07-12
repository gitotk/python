def deco(func):
    def wrapper(x):
        wx = "---" + x + "---"
        return func(wx)
    return wrapper

@deco
def printmsg(y):
    print(y, "を入力しました")

str = input("メッセージを入力：")

printmsg(str)

