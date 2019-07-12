class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

pr = Person("鈴木",55)

n = pr.getName()
a = pr.getAge()

print(n, "さんは",a,"歳です")
