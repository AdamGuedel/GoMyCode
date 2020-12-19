import numpy as np
tab=np.random.randint(0,10,(2,5))
print("Voici le tableau:")
print(tab)
print("Voici les moyennes de chaque ligne:")
print(np.mean(tab,axis=1))