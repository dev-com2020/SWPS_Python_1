a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)
print(a & b)
print(a - b)

# nie jest mutowalny
# a.add(4)

uprawnienia = {
    frozenset(['read', 'write']): "admin",
    frozenset(['read']): "user"
}

print(uprawnienia[frozenset(['read', 'write'])])
