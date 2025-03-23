from collections import defaultdict

dd = defaultdict(int)

dd['banana'] += 5

print(dd)


def empty_matrix():
    return [[0] * 3 for _ in range(3)]


matrix_map = defaultdict(empty_matrix)

print(matrix_map["A"])
