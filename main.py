from klasy.Animal import Animal, Chomik
from klasy.Person import Person
from klasy.Person2 import Persona
from klasy.Person3 import Osoba
from klasy.Termometr import Termometr

osoba1 = Person("jan", "kowalski")
osoba2 = Persona("janina", "kowalska")
osoba3 = Osoba("Tomek", 1983)
ter1 = Termometr()
zw1 = Animal("burek")
print(zw1.speak())
zw2 = Chomik("stefan", "brown")
print(zw2.speak())

print(osoba1.powitanie())
print(osoba1)
print(osoba2.powitanie())
print(osoba2)
osoba3.age = 25
print(osoba3.age)
# ter1.celsius = -344
ter1.celsius = 30
print(ter1)
print(Chomik.__mro__)