from operator import itemgetter, attrgetter

x=[(2,5), (1,2), (4,4), (2,3), (2,1)]
x.sort(key=itemgetter(1))
print(x)