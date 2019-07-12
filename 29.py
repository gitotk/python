class Person:
    count = 0

    def __init__(self, name, age):
        Person.count = Person.count + 1
        
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    @classmethod
    def getCount(cls):
        return cls.count

pr1 = Person("鈴木",55)
pr2 = Person("田中",33)

print(pr1.getName(), "さんは",pr1.getAge(),"歳です")
print(pr2.getName(), "さんは",pr2.getAge(),"歳です")
print("合計：", Person.getCount(),"名")
