import random
from pokemon import Pokemon


class Arene:
    def __init__(self, canvas):
        """
        Crées une arène
        Crées 10 pokemons dans l'arène, avec des statistiques générées aléatoirement

        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        """
        self.listeDePokemons = []
        self.running = True
        sprites = ["reptincel", "bulbizarre", "carapuce", "nodulithe", "ponchiot"]
        for i in range(80):
            temp_x = random.randint(100, 1200)
            temp_y = random.randint(120, 560)

            temp_x_vel = random.randint(8, 30) * random.choice([1, -1])
            temp_y_vel = random.randint(8, 30) * random.choice([1, -1])
            # La formule du calcul de la vélocité permet d'éviter d'avoir des valeurs trop faibles/négatives


            temp_image = random.choice(sprites)

            temp_puissance = random.randint(100, 700)

            poke = Pokemon(temp_x, temp_y, temp_image, temp_puissance, temp_x_vel, temp_y_vel, canvas)
            self.ajouter(poke)

    def ajouter(self, pokemon):
        """
        Ajoutes un pokemon a l'arène

        :param pokemon: (Pokemon) le pokemon à ajouter
        :return:
        """
        self.listeDePokemons.append(pokemon)

    def retirer_pokemon_ko(self):
        """
        Retire tout les pokemons KO de l'arène
        :return:
        """
        for poke in self.listeDePokemons:
            if poke.get_ko():
                self.listeDePokemons.remove(poke)

    def nb_pokemons(self):
        """

        :return: (int) nombre de pokemons dans l'arène
        """
        return len(self.listeDePokemons)

    def combat(self, canvas):
        """
        Trie les pokemons par leur coordonnée en x
        Vérifie les combats pour toutes les paires de pokemons consécutives

        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        liste_de_pokemons = sorted(self.listeDePokemons, key=lambda x: x.get_x())

        for i in range(len(liste_de_pokemons)-1):
            self.check_fight(liste_de_pokemons[i], liste_de_pokemons[i + 1], canvas)

    def check_fight(self, poke1, poke2, canvas):
        """
        Vérifie si les deux pokemons sont proches
        Si ils le sont:
            Le pokemon le plus puissante absorbe la puissance de l'autre
            Le pokemon le plus faible est mis KO

        Appelle retirer_pokemon_ko pour retirer le pokemon qui vient d'être éliminé

        Vérifie s'il reste un seul survivant, la partie se termine si c'est le cas

        :param poke1: (Pokemon) le premier pokemon à comparer
        :param poke2: (Pokemon) le deuxième pokemon à comparer
        :param canvas: (tkinter.Canvas) le canvas sur lequel les pokemons sont dessinés
        :return:
        """
        detection_range = 100
        if abs(poke2.get_x() - poke1.get_x()) < detection_range:
            if (abs(poke2.get_y() - poke1.get_y())) < detection_range:
                if poke1.get_puissance() >= poke2.get_puissance():
                    poke2.set_ko(True, canvas)
                    poke1.set_puissance(poke1.get_puissance() + poke2.get_puissance())
                    poke1.add_kill(canvas)
                else:
                    poke1.set_ko(True, canvas)
                    poke2.set_puissance(poke1.get_puissance() + poke2.get_puissance())
                    poke2.add_kill(canvas)

        self.retirer_pokemon_ko()

        if self.nb_pokemons() == 1:
            self.running = False
