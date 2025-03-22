from klasy.Person import Person
from klasy.Person2 import Persona
from klasy.Person3 import Osoba

osoba1 = Person("jan", "kowalski")
osoba2 = Persona("janina", "kowalska")
osoba3 = Osoba("Tomek", 1983)

print(osoba1.powitanie())
print(osoba1)
print(osoba2.powitanie())
print(osoba2)
osoba3.age = 25
print(osoba3.age)