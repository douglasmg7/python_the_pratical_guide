# j/usr/bin/env python3

l1 = [1, 2, 3, -5]
l2 = all(el > 0 for el in l1)
print(l2)

l2 = any(el > 0 for el in l1)
print(l2)
