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
  
person = Person()

atrName = input()
atrValue = input()

setattr(person, atrName, atrValue)

print(json.dumps(person, default=dumper, indent=2, ensure_ascii=False))



