from cartes import *

def cmp_carte(c1:int, c2:int) -> int:
    """
        Compare deux cartes c1 et c2.
        Renvoie 1 si c1 < c2, -1 si c1 > c2 et 0 sinon.
        
        On regarde d'abord la couleur et en cas d'égalité, on regarde la valeur.
    """
    pass

def selection(main:list) -> None:
    """
        Trie par sélection une main donnée (inplace)
        en utilisant la fonction de comparaison
    """
    n = len(main)
    
    for i in range(0, n-1):
        mini = main[i]
        for j in range(i+1, n):
            if ... :
                mini = j
                
        if mini != i:
            L[mini], L[i] = L[i], L[mini]