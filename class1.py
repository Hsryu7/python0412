#class1.py

class Person:
    def __init__(self):
        self.name="default name"
    def print(self):
        print("My name is {0}".format(self.name))


p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

#런타임시에 변수 추가(동적형식)
Person.title = "new title"

print(p1.title)
print(p2.title)
print(Person.title)