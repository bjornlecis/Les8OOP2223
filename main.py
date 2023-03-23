import operator as op

g1 = 5.1
g2 = 7
if g1 < g2:
    print("is kleiner")

if op.lt(g1,g2):
    print("kleiner")
