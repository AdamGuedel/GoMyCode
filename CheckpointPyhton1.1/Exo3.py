d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
def merge_two_dicts(d1,d2):
    z = d1.copy() 
    z.update(d2)
    return z
z = merge_two_dicts(d1,d2)
for i , g in d1.items():
    for a , b in d2.items():
        if i==a :
            print(g+b)
            z[i]=g+b
print(z)
