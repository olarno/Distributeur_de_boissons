import sys

_, billet, prix = sys.argv

billet = float(billet)
prix = float(prix)

if prix > billet :
  print(f"Pas assez, il manque {prix - billet}€")
elif prix == billet :
  print("Impecable, merci!")
else:
  trop = billet - prix 
  print(f"Merci, je dois vous rendre {trop}€ ")
  # pièces a disposition
  pièces = [2, 1, .50, .20, .10, .05, .02, .01]
  # piece rendu : une liste des pieces a rendre 
  pièces_a_rendre = []
  # tant que trop perçu est supérieur a 0 on boucle 
  pièce = pièces.pop(0)
  while trop != 0: 
    # la pièce est inférieur a ce qu'il nous rest à rendre 
    # la pièce est trop grande et du coup on vas devoir considérer une autre pièce
    if pièce > trop:
      pièce = pièces.pop(0)
    else:
      pièces_a_rendre.append(pièce)
      trop = trop - pièce
      trop = round(trop, 2)
  print("Je vous rends ces pièces là : ", pièces_a_rendre)
