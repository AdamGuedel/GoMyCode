import numpy as np
import pandas as pd
exam_data={'nom': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'tentatives': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
"qualifier": ["oui","non","oui","non","non","oui","oui","non","non","oui"] }
labels = ["a","b", "c","d","e","f","g","h","i","j"]
df = pd.DataFrame(exam_data)
print("exo1")
print(df.head(3))
print("exo2")
print(df.dropna(how = 'any'))
print("exo3")
print(df.loc[:,['nom', 'score']])
print("exo4")
new_row = {'nom' : "Suresh", " score ": 15.5, " tentatives ": 1, "qualifier": "yes"}
print(df.append(new_row, ignore_index=True))
print("exo5")
print('POP')
print( df.pop('tentatives') , df)
print("exo6")
df['succès']= np.where(df['score']> 10 ,1,0)
print(df)