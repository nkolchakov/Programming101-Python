from utils.serializers import Jsonable, Xmlable

class Panda(Jsonable, Xmlable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


def main():
    p = Panda('Ivo',12)
    xml_string = p.to_xml()
    s = Panda.from_xml(xml_string)
    print(s.age)
    person = Person(name='Rado')
    print(Panda.from_json(person.to_json())) 

if __name__ == '__main__':
    main()



