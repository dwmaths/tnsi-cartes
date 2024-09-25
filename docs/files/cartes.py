def creer_carte(c:int, v:int) -> int:
    """
        Crée une carte de couleur c et de valeur v.
        
        >>> creer_carte(0b01, 0b110)
        >>> 14
        
        14 représente le Roi de Coeur
    """
    pass

def couleur(carte:int) -> int:
    """
        Renvoie la couleur d'une carte passée en paramètre :
        (0:Carreau, 1:Coeur, 2:Pique, 3:Trèfle)
        
        >>> couleur(14)
        >>> 1
    """
    pass

def valeur(carte:int) -> int:
    """
        Renvoie la valeur d'une carte passée en paramètre :
        (0:7, 1:8, 2:9, 3:10, 4:V, 5:D, 6:R, 7:As)
        
        >>> valeur(14)
        >>> 6
    """
    pass

def voir_carte(carte:int) -> str:
    """
        Représentation d'une carte
    """
    COULEURS = ["♦", "♥", "♠", "♣"]
    VALEURS  = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    
    return VALEURS[valeur(carte)] + ' de ' + COULEURS[couleur(carte)]

def creer_jeu() -> list:
    """
        Renvoie la liste des cartes d'un jeu classique.
    """
    res = []
    for c in range(4) :
        for v in range(8) :
            res.append(creer_carte(c, v))
    return res