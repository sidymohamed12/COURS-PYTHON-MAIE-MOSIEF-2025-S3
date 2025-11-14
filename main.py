#  ======== MODE DE MANIPULATION DE FICHIERS ==========

# mode lecture -> r => reading => pour la lecture de fichier
# mode ecriture -> w => writing => permet d'ecrire dans un fichier mais supprime le fichier avant d'ecrire
# mode ajout -> a => append => ajoute à la fin du fichier

#  ======== OPERATIONS A REALISER ==========

# CRUD => Create, Read, Update, Delete

# ============ VARIABLES POUR LES MODES =========

modeLecture = "r"
modeEcrire = "w"
modeAjouter = "a"

# ============ VARIABLES POUR LES FICHIERS =========

fileUsers = r"users.txt"
filePlats = r"plats.txt"

# ============= CARACTERISTIQUES DES ENTITES =============

# ============ UTILISATEURS =========

# 1. nom complet
# 2. telephone
# 3. mot de passe
# 4. role (ADMIN, VENDEUR, RESTAURATEUR)
# 5. etat (1 = actif, 0 = inactif)

# ============ PLATS =========

# 1. nom
# 2. qte
# 3. prix
# 4. ingredients
# 5. disponibilité (1 = disponible, 0 = non disponible)

# ============ EXPLICATION DU .SPLIT() =========

# le .split() permet de séparer une chaine de caractere en plusieurs parties -> retourne une liste
# il prend en parametre le caractere qui va servir de séparateur


# ligne = "ameth ba:781234567:passer:ADMIN:1" 
# ligne.split(":") => ['ameth ba', '781234567', 'passer', 'ADMIN', '1']

# [
    # 0 -> 'ameth ba', 
    # 1 -> '781234567', 
    # 2 -> 'passer', 
    # 3 -> 'ADMIN', 
    # 4 -> '1'
# ]


# ============ EXPLICATION DU .JOIN() =========

# le .join() permet de réunir plusieurs chaines de caractere en une seule -> retourne une chaine de caractere

# liste = ['ameth ba', '781234567', 'passer', 'ADMIN', '1']
# ":".join(liste) => 'ameth ba:781234567:passer:ADMIN:1'

# ============= EXPLICATION DU STRIP() =============

# le .strip() permet de supprimer un caractere donné au debut et a la fin d'une chaine de caractere
# il prend en parametre le caractere qu'on veut supprimer

# par defaut si on ne lui donne rien en parametre, il supprime les espaces, les tabulations et les retours a la ligne au debut et a la fin de la chaine

# exemple :

# nom = "        sidy mohamed        "
# print("avant : ", nom)
# print("apres : ", nom.strip())

# ============ FONCTIONS DE RECUPRATION DES DONNES =========

# 1. recuprer les utilisateurs
def get_non_user(ligne):
      nom=ligne.split(":")[0].strip()
      return nom 

def get_telephone_user(ligne):
      tel=ligne.split(":")[1].strip()
      return tel 

def get_motpass_user(ligne):
     mot=ligne.split(":")[2].strip()
     return mot 

def get_role_user(ligne):
     role=ligne.split(":")[3].strip()
     return role 


def get_etat_user(ligne):
      etat=ligne.split(":")[4].strip()
      return etat


# 2. recuprer les plats
def get_nom_plat(ligne):
    return ligne.split(":")[0].strip()
    
def get_qte_plat(ligne):
    liste = ligne.split(":")
    return liste[1].strip()

def get_prix_plat(ligne):
    liste = ligne.split(":")
    return liste[2].strip()
    

def get_ingeredients_plat(ligne):
    liste = ligne.split(":")
    return liste[3].strip()

def get_disponibilite_plat(ligne):
    liste = ligne.split(":")
    return liste[4].strip()


# ligne = "lakh: 22: 750: mil,sow,sucre,raisin: 1"

# print (get_ingeredients_plat(ligne))


# ========== FONCTIONS D'AFFICHAGE DES DONNEES ==========

def afficher_users():
    print("=" * 50)
    print("AFFICHAGE DES UTILISATEURS")
    print("=" * 50)
    
    with open(fileUsers, modeLecture) as file:
        # file = # ameth ba:781234567:passer:ADMIN:1
                # assane ndiaye:771234567:passer:VENDEUR:1
                # roronoa zoro:761234567:passer:RESTAURATEUR:1
                # birane ndiaye:701234567:passer:ADMIN:0
        
        lignes = file.readlines()
        
        if not lignes:
            print("il n'y a aucun utilisateur")
            return
        
        cpt = 0
        for ligne in lignes:
            # ligne = # ameth ba:781234567:passer:ADMIN:1
            cpt = cpt + 1
            nom = get_non_user(ligne) # -> nom = "ameth ba"
            tel = get_telephone_user(ligne)
            mot = get_motpass_user(ligne)
            role = get_role_user(ligne)
            etat_recuperer = get_etat_user(ligne)
            etat = "actif" if etat_recuperer == "1" else "inactif"
            
            print("-" * 50)
            print(f"utilisateur n° {cpt}")
            print(f"nom : {nom}, telephone : {tel}, mot de passe : {mot}, role : {role}, etat : {etat}")
            print("-" * 50)
            
    file.close()

# afficher_users()

# afficher_plats
def afficher_plat():
    print("=" *50)
    print("AFFICHAGE DES PLATS")
    print("=" *50)
    with open(filePlats,modeLecture) as file:
        lignes = file.readlines()
        
        if not lignes:
            print("pas de plats")
            return

        cpt = 0 
        for ligne in lignes:
            cpt = cpt + 1
            nom = get_nom_plat(ligne)
            qte = get_qte_plat(ligne)
            prix = get_prix_plat(ligne)
            ingredient = get_ingeredients_plat(ligne) # -> ingredient = "mil,sow,sucre,raisin"
            disponibilite_recuperer = get_disponibilite_plat(ligne)
            disponibilite = "disponible" if disponibilite_recuperer == "1" else "non disponible"

            print("-" * 50)
            print(f"plat n° {cpt}")
            print(f"nom: {nom}, quantité: {qte}, prix: {prix}, disponibilité: {disponibilite}")
            print("les ingredients sont:")
            ings = ingredient.split(",") # -> ings = ["mil", "sow", "sucre", "raisin"]
            cpt_ing = 0
            for ing in ings:
                cpt_ing = cpt_ing + 1
                print(f"{cpt_ing}- {ing}")
            print ("-" * 50)

    file.close()

# afficher_plat()

# ========== FONCTIONS D'AJOUT DES DONNEES ==========

def ajout_plat ():
    print("=" * 50)
    print("AJOUT D'UN PLAT")
    print("=" * 50)
    
    nom = input("entrer le nom du plat : ").strip()
    qte = input("entrer la quantité du plat : ").strip()
    prix = input("entrer le prix du plat : ").strip()
    disponibilite = 1
    ings = []
    ok = input("voulez-vous ajouter des ingredients ? (o/n) : ").strip()
    while ok == "o":
        ing = input("entrer l'ingredient : ").strip()
        ings.append(ing)
        ok = input("voulez-vous ajouter des ingredients ? (o/n) : ").strip()
        
    ings = ",".join(ings)
    
    with open(filePlats, 'a') as file:
        file.write(f"{nom}:{qte}:{prix}:{ings}:{disponibilite}")
    file.close()
    print("le plat a bien ete ajouté")
    
ajout_plat()

