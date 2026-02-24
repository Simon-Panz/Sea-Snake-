from pyghthouse import Pyghthouse
from lighthouse_login import username, token
import pgzrun
import random
from time import sleep
from Funktionen_für_Seasnake import *
# Lege Bildschirmgröße für Pygame Zero fest
WIDTH = 560
HEIGHT = 700

# Verbindung mit Lighthouse herstellen
#conn = Pyghthouse(username, token)
#Pyghthouse.start(conn)

# Globale Variablen für das Spiel
player = {"x": 14, "y": 7}
gamestate = "intro"	# Spielstatus zu Beginn "intro"
direction = 0		# zu Beginn keine Richtung

# Fish
fish = 0
fishlist = []

# Funktion für blauen Farbverlauf
def blue(y):
        list = (140-8*y, (155-8*y), (255-8*y))
        return list

# Zeichne Bildschirm (wird ca. 60-mal pro Sekunde aufgerufen)
def draw():
    
    global gamestate, direction
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    
    # Zeichne aktuelles Bild
    image = Pyghthouse.empty_image()

    # Titelbild
    if gamestate == "intro":
        direction = 0	# Richtung auf "none" setzen, sonst bewegt sich die Figur wieder, wenn man zurück ins Spiel geht
        gamestate_intro(image, black, blue)


    # ingame Darstellung:
    elif gamestate == "game":
        # Hintergrund darstellen:
        for y in range(14):
            for x in range(28):
                image[y][x] = blue(y)
        # Fish
        image[fishlist[0]["y"]][fishlist[0]["x"]] = (255, 102, 255)

        # Player
        image[player["y"]][player["x"]] = (255, 255, 0)
    
        sleep(0.25)		#Geschwindigkeit vom Player
        # Bewege Spielfigur nach links, wenn Richtung = "left":
        if direction == "left":
            if player["x"] == 0:
                gamestate = "gameover"
            elif player["x"] > 0:
                player["x"] -= 1
        # Bewege Spielfigur nach rechts, wenn Richtung = "right":
        elif direction == "right":
            if player["x"] == 27:
                gamestate = "gameover"
            elif player["x"] < 27:
                player["x"] += 1
        # Bewege Spielfigur nach unten, wenn Richtung = "down":
        elif direction == "down":
            if player["y"] == 13:
                gamestate = "gameover"
            elif player["y"] < 13:
                player["y"] += 1
        # Bewegt Spielfigur nach unten, wenn Richtung = "down"
        elif direction == "up":
            if player["y"] == 0:
                gamestate = "gameover"
            elif player["y"] > 0:
                player["y"] -= 1

    # Game Over Screen
    elif gamestate == "gameover":
        direction = 0	# Richtung wieder am 0 setzen
        gamestate_gameover(image, black, red)

    # Schicke aktuelles Bild an Lighthouse-Server
    #Pyghthouse.set_image(conn, image)

    # Stelle Bild zusätzlich im Pygame-Fenster dar
    screen.clear()
    for y in range(14):
        for x in range(28):
            screen.draw.filled_rect(Rect(x*20, y*50, 20, 30), image[y][x])
            screen.draw.rect(Rect(x*20, y*50, 20, 30), (50, 50, 50))


# Verarbeite gedrückte Taste (wird bei Tastendruck aufgerufen)
def on_key_down(key):
    global gamestate, direction
    # Beendet Programm, falls Escape-Taste gedrückt wurde
    if key == keys.ESCAPE and gamestate == "intro":
        Pyghthouse.close(conn)
        exit()
    # Mit Escape-Taste kommt man zurück zum Titelbild, falls man im Spiel ist
    elif key == keys.ESCAPE and gamestate == "game":
        gamestate = "intro"
    # Mit Space-Taste kommt man ins Spiel, wenn man gerade nicht im Spiel ist
    elif key == keys.SPACE and gamestate != "game":
        gamestate = "game"
        player["x"] = 14
        player["y"] = 7
        direction = 0
    # Richtung nach links ändern
    elif key == keys.LEFT or key == keys.A:
        direction = "left"
    # Richtung nach rechts ändern
    elif key == keys.RIGHT or key == keys.D:
        direction = "right"
    # Richtung nach unten ändern
    elif key == keys.DOWN or key == keys.S:
        direction = "down"
    # Richtung nach oben ändern
    elif key == keys.UP or key == keys.W:
        direction = "up"


# Aktualisiere Spielzustand (wird ca. 60-mal pro Sekunde aufgerufen)
def update(dt):
    global gamestate
    global fish
    global fishlist
    global player

    # Fish
    def fishcheck():
        global fishlist
        global fish
        if fish == 0:
            fish += 1
            for n in range(fish):
                n = {"x": random.randint(0, 27), "y": random.randint(0, 13)}
                fishlist.append(n)

    fishcheck()
    # CONSUME
    if fishlist[0]["y"] == player["y"] and fishlist[0]["x"] ==  player["x"]:
        fish -= 1
        fishlist.pop(0)
    fishcheck()
    pass


# Starte Pygame Zero
pgzrun.go()
