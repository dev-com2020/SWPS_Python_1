from collections import Counter

c1 = Counter("liczymy wystąpienia w string")
c2 = ["apple", "banana", "orange", "banana", "orange", "banana"]
print(c1)
print(Counter(c2))
print(Counter(c2).most_common(1))
l1 = Counter(a=2, b=3)
print(list(l1.elements()))

c3 = Counter("hello")
c3.update("hello")
c3.subtract("o")
print(c3)

licznik2 = Counter(a=3, b=1)
licznik3 = Counter(a=1, b=2)

print(licznik2 + licznik3)
print(licznik2 - licznik3)
print(licznik2 & licznik3)
print(licznik2 | licznik3)

