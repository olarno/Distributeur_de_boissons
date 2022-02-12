import sys 

# on récupérer les arguments (affichage_distro.py X Y)
# X = monnaie donnée par le client 
# Y = prix du produit 
_, *arguments = sys.argv
monnaie, prix = arguments

# on convertis les arguments en float
monnaie = float(monnaie)
prix = float(prix)

# On compare nos deux valeurs afin de connaitre l'affichage 
# monnaie < prix = manque de l'argent (X)
# monnaie == prix = pile poil merci 
# monnaie > prix = merci rendre monaie (X)
# CUSTOM : Ajout du montant rendu ou montant manquant
if monnaie < prix :
  monnaie_supplement = prix - monnaie
  print("Vous devez ajouter de la monnaie.")
  print(f"Il manque : {monnaie_supplement}€")
elif monnaie == prix :
  print("Merci!")
  print("A bientôt!")
elif monnaie > prix :
  monnaie_rendu = monnaie - prix 
  print("Merci!")
  print(f"Nous vous rendons {monnaie_rendu}€! Pensez bien à les récuperer!")
else :
  print("Erreur machine")