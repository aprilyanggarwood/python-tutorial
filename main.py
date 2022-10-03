from test import *



ed = Person("Ed", 40)
ted = Person("Ted", 25)
print(ed)
print(type(ed))
print("Name: ", ed.name)
print("Age: ", ed.age)
print("Name: ", ted.name)
print("Age: ", ted.age)

print(ed.__str__())

doggo = Dog("Fido", 3)
doggo.greet()

rect = Rectangle(3, 4)
print(rect.color)
print(rect.length)
print(rect.width)