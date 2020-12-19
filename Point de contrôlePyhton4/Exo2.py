import numpy as np
tab=np.random.randint(0,10,(5,5))
stab= np.asarray(tab)
print("Le tableau:")
print(tab)
print("La diagonale:")
print(np.diagonal(stab))
print("La somme:")
print((np.trace(stab)))