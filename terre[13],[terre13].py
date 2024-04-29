def est_triee(liste):
    return all(liste[i] <= liste[i+1] for i in range(len(liste)-1))


liste1 = [1, 2, 3, 4, 5]

liste2 = [5, 3, 2, 1]

print("La liste 1 est triée." if est_triee(liste1) 
    else "La liste 1 n'est pas triée.")
print("La liste 2 est triée." if est_triee(liste2) 
    else "La liste 2 n'est pas triée.")