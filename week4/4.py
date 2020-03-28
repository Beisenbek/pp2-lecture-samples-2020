import json
class Person:
    def __init__(self):
        self.name = "John"
        self.age = 36
        self.country = "Norway"

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
        
delattr(Person, 'age')

person = Person()

print(json.dumps(person, default=dumper, indent=2, ensure_ascii=False))


# The Person object will no longer contain an "age" property
