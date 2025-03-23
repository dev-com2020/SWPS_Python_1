from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
User = namedtuple("User", "id name email")
User.__new__.__defaults__ = (None, "nieznany", "no email")

point = Punkt(3, 4)
print(point.x)
print(point.y)
print(point)

user1 = User(1, "tomek", "tomek@on.pl")
user2 = User()

print(user2.email)

# rozpakowanie działa
x1, y2 = point

# nie da się zmienić wartości
# point.x = 1123
