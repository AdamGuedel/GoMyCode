n_prix=int(input())

if n_prix >= 500 :
    print(float(n_prix*(50/100)))

elif 200 <= n_prix < 500  :
    print(float(n_prix-(n_prix*(30/100))))

elif n_prix < 200 :
    print(float(n_prix-(n_prix*(10/100))))