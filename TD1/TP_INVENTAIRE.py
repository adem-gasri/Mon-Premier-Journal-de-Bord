def calculer_valeur_stock(inventaire, prix_unitaires):
    total = 0
    indices = 0

# ERREUR 1 : Une boucle infinie se cache ici
    while indices < len(inventaire):
        produit = inventaire[indices]
        indices = indices + 1

# ERREUR 2 : Problème d'accès au dictionnaire (Case sensitive)
        prix = prix_unitaires[produit]

        total += prix
# Quelque chose manque ici pour faire avancer la boucle...
    return total

def main():
# Liste des produits en rayon
    mon_stock = ["console", "Manette", "Jeu"]

# Catalogue des prix (Attention aux clés !)
    catalogue = {
        "console": 300,
        "Manette": 50,
        "Jeu": 60
    }

    print("Analyse du stock en cours...")
    resultat = calculer_valeur_stock(mon_stock, catalogue)
    print(f"Valeur totale du stock : {resultat}€")

if __name__ == "__main__":
    main()