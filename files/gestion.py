from cartes import *

def melanger_jeu(jeu:list) -> None:
    """
        Mélange le jeu inplace.
    """
    pass

def distribution(jeu:list, nbj:int, nbc:int) -> dict:
    """
        jeu : la liste des cartes
        nbj : le nombre de joueurs
        nbc : le nombre de cartes par joueurs
        
        Attention : la liste jeu doit se vider des cartes distribuer.
    """
    res = {} # Le dictionnaire des joueurs
    
    if ... <= ...: # Il est possible de distribuer
        
        for i in range(1, nbj+1): # On distribue joueur par joueur
            res[f"Joueur {i}"] = ... # Jeu vide pour commencer
            
            for j in range(...): # On distribue nbc cartes
                res[f"Joueur {i}"].append(...)
                
    return res
    
def voir_mains(joueurs:dict) -> str:
    """
        Observation des mains des joueurs.
    """
    res = ""
    
    for elt in joueurs:
        res += f"{elt} : " + " - ".join([voir_carte(c) for c in joueurs[elt]]) + '\n'
        
    print(res[:-1])