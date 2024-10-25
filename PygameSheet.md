# Pygame Cheatsheet

## Initialisation et Fermeture
- **`pygame.init()`** : Initialise tous les modules Pygame.
- **`pygame.quit()`** : Ferme Pygame et libère les ressources.

## Fenêtre et Affichage
- **`pygame.display.set_mode((largeur, hauteur))`** : Crée une fenêtre de dimensions spécifiées.
- **`pygame.display.set_caption("Titre")`** : Définit le titre de la fenêtre.
- **`pygame.display.flip()`** : Met à jour tout l'écran.
- **`pygame.display.update(rectangle)`** : Met à jour la partie spécifiée de l'écran.

## Gestion des Événements
- **`pygame.event.get()`** : Récupère la liste des événements.
- **`pygame.event.poll()`** : Récupère le prochain événement de la file d'attente.
- **`pygame.event.clear()`** : Vide la file des événements.
- **`pygame.event.wait()`** : Attend jusqu'à ce qu'un événement soit disponible.

## Gestion du Temps
- **`pygame.time.Clock()`** : Crée un objet horloge pour contrôler le temps.
- **`clock.tick(fps)`** : Maintient la boucle à une fréquence de rafraîchissement spécifiée (ex : 60 FPS).

## Dessiner des Formes
- **`pygame.draw.line(surface, couleur, début, fin, épaisseur)`** : Dessine une ligne.
- **`pygame.draw.rect(surface, couleur, rect)`** : Dessine un rectangle.
- **`pygame.draw.circle(surface, couleur, centre, rayon)`** : Dessine un cercle.
- **`pygame.draw.ellipse(surface, couleur, rect)`** : Dessine une ellipse.
- **`pygame.draw.polygon(surface, couleur, points)`** : Dessine un polygone.

## Images et Surfaces
- **`pygame.image.load("chemin_image")`** : Charge une image.
- **`surface.blit(image, position)`** : Dessine l'image sur la surface spécifiée.
- **`pygame.Surface((largeur, hauteur))`** : Crée une surface vide.

## Gestion du Texte
- **`pygame.font.Font("chemin_police", taille)`** : Crée un objet police avec la taille spécifiée.
- **`font.render(texte, antialias, couleur)`** : Rend un texte sur une surface.

## Gestion du Clavier et de la Souris
- **`pygame.key.get_pressed()`** : Récupère l'état de toutes les touches du clavier.
- **`pygame.mouse.get_pos()`** : Récupère la position actuelle de la souris.
- **`pygame.mouse.get_pressed()`** : Récupère l'état des boutons de la souris.

## Sons et Musique
- **`pygame.mixer.Sound("chemin_son")`** : Charge un son.
- **`sound.play()`** : Joue un son.
- **`pygame.mixer.music.load("chemin_musique")`** : Charge un fichier musical.
- **`pygame.mixer.music.play(-1)`** : Joue la musique en boucle.

## Collision et Gestion des Rectangles
- **`pygame.Rect(x, y, largeur, hauteur)`** : Crée un objet rectangle.
- **`rect.colliderect(autre_rect)`** : Vérifie si deux rectangles se chevauchent.
- **`rect.collidelist(liste_rects)`** : Vérifie les collisions avec une liste de rectangles.

