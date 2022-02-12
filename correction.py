import sys 
 
if len(sys.argv) != 3:
    print('Erreur: pas le bon nombre d\'arguments. Reçu', len(sys.argv) - 1)
    print('Attendu : 2 (le premier est le billet introduit, le second le prix.)')
    exit()

_, billet, prix = sys.argv
billet = float(billet)
prix = float(prix)
print (f"Vous avez donné {billet}€ pour un produit qui coûte {prix}")

if billet < prix:
  manque = prix - billet 
  print(f'Il manque {manque}€')
  print('Rajoutez un billet s\'il vous plait')
else : 
  if billet == prix:
    print('C\'est parfait merci, bonne dégustation')
  else : 
    trop = billet - prix
    print(f'Merci je dois vous rendre {trop}€')


# 1) récuperer les arguments depuis la ligne de commande 
# 2) convertir les args en nombre 
# 3) tester si il manque de l'argent 
# 3.a) si c'est le cas afficher le montant qu'il manque + msg 
# 3.b) afficher puis arreter 
# 4) doit on rendre de la monaie  ou pas ?
# 4.a) on ne doit pas rendre (pile)
# 4.b) on affiche merci, aurevoir 
# 4.c) on doit rendre 
# 4.d) combien doit on rendre 
# 4.e) afficher merci, je vous rend le montant 