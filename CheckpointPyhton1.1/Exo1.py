def mult(liste):
    r = 1
    for element in liste:
        r *= element
    return r
 
x = [2,3,6]
print (mult(x))