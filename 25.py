a = 0

def funcB():
    b = 1

    print("funcBのなかでは変数aと変数bが使えます")
    print("変数aは",a)
    print("変数bは",b)

def funcC():
    c = 2

    print("funcCのなかでは変数aと変数cが使えます")
    print("変数aは",a)
    print("変数cは",c)


print("関数の外では変数aが使えます",a)

funcB()
funcC()

    


