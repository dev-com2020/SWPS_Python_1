from itertools import (count, cycle,
                       repeat, chain, islice, compress, permutations, combinations, product, groupby)

for i in count(10):
    print(i)
    if i >= 15:
        break

# cykl - iteracja bez końca - korzystaj z limitem
# for x in cycle("ABC"):
#     print(x)

for x in repeat('hej', 3):
    print(x)

print(list(chain([1, 2], [3, 4], [5])))
print(list(islice(count(10), 5)))

data = ['a', 'b', 'c', 'd']
selectors = [1, 0, None, 0]

print(list(compress(data, selectors)))

print(list(permutations([1, 2, 3], 2)))
print(list(combinations([1, 2, 3], 2)))
print(list(product([1, 2], repeat=2)))

data = "ABBBBBABBBCCCDAA"
grouped = groupby(data)

for key, group in grouped:
    print(key, list(group))

