from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

od.move_to_end('a')
od.move_to_end('b', last=False)

print(od)