x = 2
y = 3

l1 = [(x, y+i) for i in range(3)]
print("l1 = {l}".format(l=l1))

l2 = [(a+1, b) for (a, b) in l1]
print("l2 = {l}".format(l=l2))

l3 = l1 + l2
print("l3 = {l}".format(l=l3))

l4 = [(a, b+1) for (a, b) in l1]
print("l4 = {l}".format(l=l4))


refList = [1, -1]
l5 = [(a, b+i) for (a, b) in l1 for i in refList]
print("l5 = {l}".format(l=l5))

l6 = list(set(l5))
print("l6 = {l}".format(l=l6))

