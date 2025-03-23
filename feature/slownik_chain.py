from collections import ChainMap

a = {"x": 1, "y": 2}
b = {"x": 999, "y": 3}

cm = ChainMap(a, b)
cm['y'] = 456
new_cm = cm.new_child()
new_cm['x'] = 3
print(cm['y'])
print(new_cm)
