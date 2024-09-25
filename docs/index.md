# Jeux de cartes

## Modélisation

Une carte est un objet de la vie courante qui possède deux caractéristiques :

- une couleur parmi : Carreau, Coeur, Pique, Trèfle ;
- une valeur parmi : 7, 8, 9, 10, V, D, R, As ;

<center>
    <img src="./images/cartes.png" alt="image" width="400" height="auto">
</center>

On pourrait aisément représenter une carte à l'aide d'un **tuple nommé** ou encore d'un **dictionnaire** mais on décide de **coder** chacune de ces
cartes à l'aide d'un entier. Pour associer un entier à une carte (en gardant une certaine cohérence), on décide d'utiliser un **mot binaire**.

### Mot binaire

On commence par rappeler quelques détails techniques en Python :

!!! question "Quelques opérateurs binaires"

    1. Écrire l'instruction `a = 0b10010110` et vérifier qu'il est bien égal à `150`.

        ??? note

            On rappelle que $a = 1\times 2^1 + 1\times 2^2 + 1\times 2^4 + 1\times 2^7 = 150$.

    2. Si on souhaite récupérer les quatre bits de poids faibles, on effectue un **ET LOGIQUE** comme dans l'instruction `a & 0b00001111`.  
    Tester cette instruction et vérifier que l'on obtient `6`

        ??? note

            Si on écrit `6` en binaire (à l'aide de l'instruction `bin(6)`), on obtient `0b110` que l'on peut aussi écrire `0b0110`.

    3. Vérifier que l'instruction `a & 240` renvoie le nombre `144` et essayer de comprendre pourquoi.

        ??? tip "Indication"

            Peut-être faudrait-il convertir `240` en binaire pour comprendre.

        ??? bug "Attention"

            En réalité, on n'obtient pas les quatre bits de poids forts ici. En effet, le mot est complété par quatre zéros.  
            Pour supprimer ces quatre zéros, il faut décaler le mot obtenu de quatre bits vers la droite.  

            Tester l'instruction `144 >> 4` et vérifier qu'en binaire le résultat s'écrit `0b1001`.

    4. Vérifier que l'instruction `0b1001 << 4 | 0b0110` permet de retrouver le nombre de départ.

        ??? note

            L'opérateur `|` est un **OU LOGIQUE**.

Pour modéliser une carte, il nous faut donc :

- une couleur (parmi quatre possibles) ;
- une valeur (parmi huit possibles).

On utilise alors un mot binaire de la forme 

<center>
<h3>0bCCVVV</h3>
</center>

car il nous faut 2 bits pour la couleur ($2^2 = 4$) et 3 bits pour la valeur ($2^3 = 8$).  

On décide alors des correspondances entre mot binaire et couleur de carte avec le tableau :

| **Couleur** | Carreau | Coeur | Pique | Trèfle |
|:-----------:|:-------:|:-----:|:-----:|:------:|
| **Binaire** | 00      | 01    | 10    | 11     |

De la même façon, on décide de l'association pour les valeurs :

| **Valeur**  | 7   | 8   | 9   | 10  | V   | D   | R   | As  |
|:-----------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Binaire** | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |

Pour commencer, vous êtes invité à télécharger le fichier  [cartes.py](<./files/cartes.py>).

!!! question "Implantation"

    1. Implanter la fonction `creer_carte(c:int, v:int) -> int` qui renvoie l'entier dont l'écriture en binaire correspond au modèle choisi ci-dessus.

        ??? tip "Indications"

            Même si les variables `c` et `v` sont des entiers, on peut leur appliquer des opérations binaires.  
            Attention, il faudra décaler des bits vers la gauche cette fois !

    2. Implanter les fonctions `couleur(carte:int) -> int` et `valeur(carte:int) -> int` qui renvoient respectivement la couleur et la valeur de la carte.

        ??? tip "Indications"

            C'est le moment d'appliquer des masques et de faire des décalages de bits !

    3. Tester alors l'instruction `voir_carte(14)` qui doit renvoyer `"Roi de ♥"`.

??? bug "Correction"

    1. On propose la fonction :

        ``` python title="Création d'une carte" linenums="1"

        def creer_carte(c:int, v:int) -> int:
            """
                Crée une carte de couleur c et de valeur v.
            """
            return (c << 3) | v
        ```

    2. On propose :

        ``` python title="Couleur d'une carte" linenums="1"

        def couleur(carte:int) -> int:
            """
                Renvoie la couleur d'une carte.
            """
            return (carte & 0b11000) >> 3
        ```

        et aussi 

        ``` python title="Valeur d'une carte" linenums="1"

        def valeur(carte:int) -> int:
            """
                Renvoie la valeur d'une carte.
            """
            return carte & 0b00111
        ```

### Mélange et distribution

Vous avez pu constater la présence de la fonction `creer_jeu() -> list` qui permet de récupérer la liste complète de toutes les cartes d'un jeu. Vous pouvez
d'ailleurs tester l'instruction `L = creer_jeu()` et ensuite jouer avec la fonction `voir_carte(carte:int) -> str` pour observer cette liste.  

Par exemple, l'instruction `[voir_carte(k) for k in range(8)]` montre les **carreaux**.

À présent, vous êtes invité à télécharger le fichier  [gestion.py](<./files/gestion.py>).

!!! question "Gestion d'un jeu"

    1. Pour implanter la fonction `melanger_jeu(jeu:list) -> None`, on propose l'algorithme suivant :

        ``` python title="Mélange d'un jeu" linenums="1"

        Pour chaque carte de la liste

            échanger cette carte avec une autre choisie aléatoirement.
        ```

        ??? tip "Indication"

            N'oubliez pas d'importer la fonction `randrange` du module `random`.

    2. On s'intéresse à présent à la distribution des cartes.  
    Pour cela, on cherche à implanter la fonction `distribution(jeu:list, nbj:int, nbc:int) -> dict`.

        a. Il n'est pas possible de distribuer les cartes quand il n'y en a pas assez.  
        Compléter le début du code pour gérer cette contrainte.

        b. La fonction doit renvoyer un dictionnaire de la forme :

        ``` python title="Dictionnaire des joueurs" linenums="1"

        { "Joueur 1" : [...],
          "Joueur 2" : [...],
          "Joueur 3" : [...], ... }
        ```

        Compléter le code proposé.

        ??? tip "Indication"

            Pour retirer le premier élément d'une liste `L`, on peut utiliser l'instruction `L.pop(0)`.

    3. Tester les instructions suivantes :

        ``` python title="Observations" linenums="1"

        >>> jeu = creer_jeu()
        >>> melanger_jeu(jeu)
        >>> joueurs = distribution(jeu, 4, 5)
        >>> voir_mains(joueurs)
        ``` 

??? bug "Correction"

    1. On propose le code :

        ``` python title="Mélange d'un jeu" linenums="1"

        from random import randrange

        def melanger_jeu(jeu:list) -> None:
            """
                Mélange le jeu inplace.
            """
            n = len(jeu)
            for i in range(n):
                j = randrange(0, n)
                L[i], L[j] = L[j], L[i]
        ```

    2. On propose le code :

        ``` python title="Distribution entre les joueurs" linenums="1"
        def distribution(jeu:list, nbj:int, nbc:int) -> dict:
            """
                jeu : la liste des cartes
                nbj : le nombre de joueurs
                nbc : le nombre de cartes par joueurs
                
                Attention : la liste jeu doit se vider des cartes distribuées.
            """
            res = {} # Le dictionnaire des joueurs
            
            if nbj*nbc <= len(jeu) : # Il est possible de distribuer
                
                for i in range(1, nbj+1): # On distribue joueur par joueur
                    res[f"Joueur {i}"] = [] # Jeu vide pour commencer
                    
                    for j in range(nbc): # On distribue nbc cartes
                        res[f"Joueur {i}"].append(jeu.pop(0))
                        
            return res
        ```

## Trier sa main

Il est courant d'avoir à trier ses cartes une fois reçues. De façon habituelle, on commence souvent par :

- organiser ses cartes par couleur ;
- organiser ensuite ses cartes par valeur ;

À présent, vous êtes invité à télécharger le fichier  [tris.py](<./files/tris.py>).

!!! question "Pour terminer"

    1. Compléter la fonction permettant de comparer les cartes.
    2. Compléter la fonction permettant le tri par sélection d'une main d'un joueur.