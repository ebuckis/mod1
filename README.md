# Mod 1

## 1. Parsing du fichier
Coordonnées 3 dimensions à enregistrer  
Input 5 et 20 points

## 2. Algo map
Tous les bords sont a une altitude de 0  
Les reliefs doivent etre des courbes (pas comme FDF)
Algo courbe, surface Bézier, NURBS, ... ?
Ou on réutilise l'algo de l'eau avec contraintes au sommmet et quelques itérations et petit coef pour dessiner la map du terrain

## 3. Simulation de l'eau
Creation des algo pour les différents types de simulations 
On utilise l'algo height fields, cf. page2 slide du haut pdf NVIDIA  
Une matrice 2d pour la hauteur d'eau 
Une matrice 2d pour la vitesse de l'eau 
Pour chaque incrément de temps, on calcul la nouvelle matrice de vitesse puis la nouvelle matrice de hauteur 
On multiplie la vitesse par un coef < 1 sinon pas de stabilité, les vagues ne s'arrêtent jamais 
Coef entre 0.9 et 0.95 selon le résultat voulu 
Seul les conditions de hauteur imposées vont varier selon les cas ci-dessous. 

### 3.1 Remplissage depuis le bas
On ajoute de la hauteur d'eau partout sur la carte par les bords
L'algo ne sert à rien dans ce cas sauf si il y a un cratère (point bas entouré de point haut)
Idem en cas de vidange par les bords, les cratères restent remplis ?

### 3.2 Vague
On fixe la hauteur d'eau sur un coté de la map  
Répartition de l'eau jusqu'a la stabilité

### 3.3 Pluie
On impose des hauteurs d'eau sur des mailles alléatoires de la carte à chaque frame pour simuler la pluie

#### 3.4 Gestion des mouvements d'eau à proximité du sol 
Profondeur nulle : Eau qui ruisselle ou eau qui grimpe sur les collines avec de la vitesse

## 4. Visuel
Utilisation d'une bibliotheque graphique pour la modélistation du terrain  
Box type aquarium  
Mise en place de couleurs en fonction de l'altitude  
Modelisation de l'eau  
Positionnement de la caméra  
Rotation, translation
Graduation x, y, z ?
Mise a l'échelle  
Activation de chaque scénario et modification des parametres via bouton + slider ou dans les arguments de lancement du programme ?

## 5. Optimisation temps de calcul pour un rendu fluide et un maillage précis
Language compilé C ou C++ ?
Multi Threading ?
OpenGL GPU ?
OpenCL ?
