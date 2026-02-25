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
player = [{"x": 14, "y": 7}]
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
    
    global gamestate, direction, player
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    gelb = (255, 255, 102)

    
    # Zeichne aktuelles Bild
    image = Pyghthouse.empty_image()

    # Titelbild
    if gamestate == "intro":
        direction = 0	# Richtung auf 0 setzen, sonst bewegt sich die Figur wieder, wenn man zurück ins Spiel geht
        gamestate_intro(image, gelb, blue)


    # ingame Darstellung:
    elif gamestate == "game":
        # Hintergrund darstellen:
        for y in range(14):
            for x in range(28):
                image[y][x] = blue(y)
        # Fish färben
        image[fishlist[0]["y"]][fishlist[0]["x"]] = (255, 102, 255)

        # Player färben
        for n in range(len(player)):
            if n == 0:	# Kopf ander Farbe als der Körper
                image[player[n]["y"]][player[n]["x"]] = (255, 255, 255)
            else:
                image[player[n]["y"]][player[n]["x"]] = (255, 255, 0)
    
        sleep(0.25)		#Geschwindigkeit vom Player
        
        
        
        # Bewegung der Schlange
        if direction != 0:
            head = {"x": player[0]["x"],"y": player[0]["y"]}	# head ist der neue Kopf, mit dem geprüft wird, was als nächstes passiert
            
        
            # Bewege Spielfigur nach links, wenn Richtung = "left":
            if direction == "left":
                    head["x"] -= 1
            # Bewege Spielfigur nach rechts, wenn Richtung = "right":
            elif direction == "right":
                    head["x"] += 1
            # Bewege Spielfigur nach unten, wenn Richtung = "down":
            elif direction == "down":
                    head["y"] += 1
            # Bewegt Spielfigur nach unten, wenn Richtung = "down"
            elif direction == "up":
                    head["y"] -= 1
            
            # Wenn Schlange auf Wand trifft, gameover:
            if head["x"] == -1 or head["x"] == 28 or head["y"] == -1 or head["y"] == 14:
                gamestate = "gameover"
            elif head in fishlist:	# Schlange verlängern, falls man auf Fisch trifft
                player.insert(0, head)
            else:					# Schlange bewegen, gleiche Länge
                player.insert(0, head)
                player.pop(-1)
            if head in player[1:]:		# Schlange trifft sich selbst, gameover
                gamestate = "gameover"
            
            
    
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
    global gamestate, direction, fish, fishlist, player
    # Beendet Programm, falls Escape-Taste gedrückt wurde
    if key == keys.ESCAPE and gamestate == "intro":
        Pyghthouse.close(conn)
        exit()
    # Mit Escape-Taste kommt man zurück zum Titelbild, falls man im Spiel ist
    elif key == keys.ESCAPE and gamestate == "game":
        gamestate = "intro"
    # Mit esc auch aus Gameover Screen ins Spiel zurück
    elif key == keys.ESCAPE and gamestate == "gameover":
        gamestate = "game"
    # Mit Space-Taste kommt man ins Spiel, wenn man gerade nicht im Spiel ist
    elif key == keys.SPACE and gamestate != "game":
        gamestate = "game"
        player[0]["x"] = 14
        player[0]["y"] = 7
        direction = 0
        fishlist = []
        fish = 0
        player[1:] = []
     # Richtung nach links ändern
     elif (key == keys.LEFT or key == keys.A) and direction != "right":
             direction = "left"
     # Richtung nach rechts ändern
     elif (key == keys.RIGHT or key == keys.D) and direction != "left":
             direction = "right"
     # Richtung nach unten ändern
     elif (key == keys.DOWN or key == keys.S) and direction != "up":
             direction = "down"
     # Richtung nach oben ändern
     elif (key == keys.UP or key == keys.W) and direction != "down":
             direction = "up"


# Aktualisiere Spielzustand (wird ca. 60-mal pro Sekunde aufgerufen)
def update(dt):
    global gamestate, fish, fishlist, player

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
    if fishlist[0]["y"] == player[0]["y"] and fishlist[0]["x"] ==  player[0]["x"]:
        fish -= 1
        fishlist.pop(0)
    fishcheck()
    pass


# Starte Pygame Zero
pgzrun.go()
