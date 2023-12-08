import random
import tkinter


class Pokemon:
    def __init__(self, x, y, image, puissance, x_vel, y_vel, canvas):
        """
        Crées un pokemon aux coordonnées x, y sur le canvas canvas, de base non KO, avec la puissance puissance, des
        statistiques de vitesses aléatoires, et comme sprite le fichier nommé image

        :param x: (int) la coordonnée en abcisse du pokemon
        :param y: (int) la coordonnée en ordonnée du pokemon
        :param image: (str) le nom du fichier qui contient le sprite du pokemon (sans l'extension de fichier)
        :param puissance: (int) la puissance du pokemon
        :param x_vel: (int) vélocity sur l'axe des abcisses
        :param y_vel: (int) vélocity sur l'axe des ordonnées
        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        """
        # Coordinates
        self.x = x
        self.y = y

        # Stats
        self.puissance = puissance
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.ko = False

        # Image
        self.image = tkinter.PhotoImage(file="assets/" + ("i" if self.x_vel < 0 else "") + image + ".png")
        self.image_name = image

        # Compteurs
        self.kills = 0
        self.evolutions = 0

        self.img = canvas.create_image(self.x, self.y, image=self.image)

    def get_x(self):
        """

        :return: (int) la coordonnée en abcisse du pokemon
        """
        return self.x

    def get_y(self):
        """

        :return: (int) la coordonnée en ordonnée du pokemon
        """
        return self.y

    def get_image(self):
        """

        :return: (tkinter.PhotoImage) le sprite du pokemon
        """
        return self.image

    def get_puissance(self):
        """

        :return: (int) la puissance du pokemon
        """
        return self.puissance

    def get_ko(self):
        """

        :return: (bool) l'état KO du pokemon, True si il est KO, False si il est en état de combattre
        """
        return self.ko

    def get_kills(self):
        """

        :return: (int) le nombre de kills du pokemon
        """
        return self.kills

    def set_x(self, x):
        """
        Change la coordonnée en abcisse du pokemon

        :param x: (int) la nouvelle coordonnée en abcisse du pokemon
        :return:
        """
        self.x = x

    def set_y(self, y):
        """
        Change la coordonnée en ordonnée du pokemon

        :param y: (int) la nouvelle coordonnée en ordonnée du pokemon
        :return:
        """
        self.y = y

    def set_image(self, image, canvas):
        """
        Change l'image du pokemon
        Supprime l'affichage précédent sur le canvas, réaffiche le pokemon sur le canvas

        :param image: (str) le nom du fichier qui contient le sprite du pokemon (sans l'extension de fichier)
        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        self.image = tkinter.PhotoImage(file="assets/" + image + ".png")
        canvas.delete(self.img)
        self.img = canvas.create_image(self.x, self.y, image=self.image)

    def set_puissance(self, puissance):
        """
        Change la puissance du pokemon

        :param puissance: (int) la nouvelle puissance du pokemon
        :return:
        """
        self.puissance = puissance

    def set_ko(self, ko, canvas):
        """
        Change l'état KO du pokemon
        Si il passe KO, il est supprimé de l'affichage

        :param ko: (bool) le nouvel état KO du pokemon
        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        self.ko = ko

        if self.ko:
            canvas.delete(self.img)

    def add_kill(self, canvas):
        """
        Rajoute un kill au compteur de kills

        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        self.kills += 1
        if self.kills >= 2 > self.evolutions:
            self.evoluer(canvas)

    def affiche(self, canvas):
        """
        Déplace le pokémon aux coordonnées auxquelles il est sensé se trouver

        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        canvas.move(self.img, self.x_vel, self.y_vel)

    def deplacement(self, canvas):
        """
        Actualise la vélocité du pokemon si il touche les bords
        Change les attributs x et y du pokemon en leur appliquant le vecteur déplacement

        :return:
        """
        if (100 > self.x) | (self.x > 1200):
            self.x_vel = -self.x_vel
            self.set_image(str(("i" if self.x_vel < 0 else "")) + self.image_name, canvas)

        if (120 > self.y) | (self.y > 560):
            self.y_vel = -self.y_vel

        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel

    def evoluer(self, canvas):
        """
        Fait évoluer le compteur d'évolutions et retrograde celui des kills
        Change l'image par la nouvelle image
        Fait monter la puissance du pokemon

        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        self.evolutions += 1
        self.kills -= 2

        self.image_name = self.image_name + "+"
        self.set_image(self.image_name, canvas)

        new_puissance = self.get_puissance() * (1 + (self.evolutions / 5))
        self.set_puissance(new_puissance)
