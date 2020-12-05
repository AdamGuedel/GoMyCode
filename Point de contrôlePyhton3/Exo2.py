liste=[1,2,3,4,5,6,7,8,9,10]
liste_impaire = [elt for idx, elt in enumerate(liste) if idx % 2 == 0]
liste_paire = [elt for idx, elt in enumerate(liste) if idx % 2 != 0]
print(liste_paire)
print(liste_impaire)

somme=sum(liste_paire)

def mult(liste):
    r = 1
    for element in liste:
        r *= element
    return r

print(somme)
print (mult(liste_impaire))