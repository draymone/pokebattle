# Importations
import tkinter  # Permet de gérer les graphiques
import pygame  # Permet de gérer le son
from arene import Arene  # Permet de gérer la logique

window = tkinter.Tk()  # Crée la fenetre
canvas = tkinter.Canvas(window,
                        width=1280,
                        height=1080,
                        background='lightblue')  # Crée le canvas
arene = Arene(canvas)  # Crée l'arène


def config():
    """
    Configure la fenetre en lui donnant un titre, grid le canvas
    Initialise le mixeur de son
    Lance la musique

    :return:
    """
    window.title("Poke Battle")
    canvas.grid()

    pygame.mixer.init()

    pygame.mixer.music.load("assets/music.mp3")
    pygame.mixer.music.play(-1)  # Loop -1 fait que la musique se joue en boucle à l'infini


def end_game():
    """
    Arrete la musique de combat
    Lance la musique de victoire

    :return:
    """
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/winner.mp3")
    pygame.mixer.music.play()


def on_tick():
    """
    Fonction éxécutée à chaque tick de jeu (10 tps)
    Déplace les pokemons et les affiche à leurs nouvelles coordonnées
    Fait se combattre les pokemons
    Prépare le prochain tick pour qu'il se lance après 100ms si la partie est encore en cours
    Si la partie est finie, appelle la fonction end_game


    :return:
    """
    for i in range(arene.nb_pokemons()):
        arene.listeDePokemons[i].deplacement(canvas)
        arene.listeDePokemons[i].affiche(canvas)
    arene.combat(canvas)
    if arene.running:
        canvas.after(100, on_tick)
    else:
        end_game()


config()  # Configure la fenêtre de l'application
on_tick()  # Commence le tickage

window.mainloop()  # Ligne finale
