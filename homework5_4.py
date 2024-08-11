class Buiding:
    total = 0
    def __init__(self):
        Buiding.total += 1
list = []
for i in range(40):
    fu = Buiding()
    i += 1
    list.append(fu)
    print(fu)
print(Buiding.total)