import json

class Person:
    typeName = 'myPerson' 
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
        

person1 = Person('John', 36, 'Norway')
person2 = Person('Smith', 20, 'UK')

print(json.dumps(person1, default=dumper, indent=2, ensure_ascii=False))
print(person1.typeName)
print(json.dumps(person2, default=dumper, indent=2, ensure_ascii=False))
print(person2.typeName)

