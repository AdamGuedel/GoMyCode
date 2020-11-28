from operator import itemgetter, attrgetter

x=[("item1", 12.20), ("item2",15.10), ("item3",24.5)]
x.sort(key=itemgetter(1))
x.reverse()
print(x)