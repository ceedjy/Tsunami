# Tsunami
OSEC project at University Savoie Mont Blanc
# TODO
 - [ ] interface :
   - [ ] => visualiser distance + vitesse + temps jusqu'au point
   - [x] => bouton reinitialiser la map
   - [x] => bouton qui demande si l'user veut un movie par rapport aux secondes ou par rapport aux pourcentages
   - [x] => pouvoir fermer la fenètre avec au moins une possibilité (croix, touche clavier, autre)
 - [x] calcul de la vistesse sur tout les points => sous forme de matrice pour la transformer en image (cf pls couleurs selon les vitesses)
 - [x] calcul vitesse entre 2 pts sélectionnés
 - [x] ajouter des contour sur l'image du temps (isochrones -> mot a intégrer dans le compte rendu)
 - [x] avoir un mini film avec les images du temps qui se propage, a générer avec openCV pour automatiser sa création
 - [ ] essayer de faire le tsunami en barre :
    - [ ] => faire une barre de point (entre les deux points cliqués)
    - [ ] => faire le travail des 5 images pour chauque point
    - [ ] => chercher le plus petit pour chaque case de la matrice et faire 5 new image à partir de ça
    - [ ] => recréer le gif à partir de ces 5 nouvelles images
 - [ ] optimiser le code pour qu'il soit plus rapide, open mp, paralléliser les calculs, cython
 - [x] téléchgarger le gif 
 - [ ] compte rendu
 - [ ] préparer présentation 

# Resources
OpenCV : 
https://shimat.github.io/opencvsharp_docs/html/66fb2360-14d2-3431-c0ef-1679c153cf06.htm
https://stackoverflow.com/questions/73056691/how-do-we-interpret-the-baseline-output-of-cv2-gettextsize

Line :
https://www.geeksforgeeks.org/python-opencv-cv2-line-method/

LineIterator : (Algo Bresenham)
https://amroamroamro.github.io/mexopencv/matlab/cv.LineIterator.html
https://docs.opencv.org/4.x/dc/dd2/classcv_1_1LineIterator.html

Bresenham (wiki):
https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham
