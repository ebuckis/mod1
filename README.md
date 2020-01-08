# Mod 1

## 1. Parsing du fichier
Coordonnées 3 dimensions a enregitrer  
Entre 5 et 20 points

## 2. Algo map
Tous les bords sont a une altitude de 0  
Les reliefs doivent etre des courbes (pas comme FDF)

## 3. Simulation de l'eau
Creation des algo pour les différents types de simulations
On utilise l'algo height fields, cf. page2 pdf NVIDIA 
Une matrice 2d pour la hauteur d'eau
Une matrice 2d pour la vitesse de l'eau
Pour chaque incrément de temps, on calcul la nouvelle matrice de vitesse puis la nouvelle matrice de hauteur
On multiplie la vitesse par un coef < 1 sinon pas de stabilité, les vagues ne s'arretent jamais
Coef entre 0.9 et 0.95 selon le résultat voulu

### 3.1 Remplissage depuis le bas

### 3.2 Vague
Mouvement de l'eau  
Répartition de l'eau jusqu'a la stabilité

### 3.3 Pluie
Répartition de l'eau  
Gestion de la vitesse de remplissage suivant les formes (ex: cratère)  
Débordement  

## 4. Visuel
Utilisation d'une bibliotheque graphique pour la modélistation du terrain  
Box type aquarium  
Mise en place de couleurs en fonction de l'altitude  
Modelisation de l'eau  
Positionnement de la caméra  
Mise a l'échelle  
