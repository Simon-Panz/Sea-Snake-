
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
conn = Pyghthouse(username, token)
Pyghthouse.start(conn)

# Globale Variablen für das Spiel
player = [{"x": 14, "y": 7}]
gamestate = "intro"	# Spielstatus zu Beginn "intro"
direction = 0		# zu Beginn keine Richtung
player_len = 1      # Spielerlänge zu Beginn
difficulty = "easy"
danger = False

speed = 0.25		# Geschwindigkeit der Schlange, Verzögerung in Sekunden
level = 0
wall_behavior = 1		# 1 = Schlange stirbt bei Wand, 2 = Schlange kann durch die Wand gehen und kommt an der anderen seite wieder raus

automatic = 0		# automatischer Modus, 1 = Schlange bewegt sich von alleine

# Fish
fish = 0
fishlist = []
fish_amount = 5		# Menge an Fischen
fish_move = 1		# 1 = Fische bewegen sich, 0 = Fische bewegen sich nicht

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

    # ingame Darstellung:
    if gamestate == "intro":
        gamestate_intro(image, gelb, blue)
    elif gamestate == "game":
        # Hintergrund darstellen:
        for y in range(14):
            for x in range(28):
                image[y][x] = blue(y)
        # Fish färben
        for n in range(len(fishlist)):
            image[fishlist[n]["y"]][fishlist[n]["x"]] = (255, 102, 255)

        # Player färben
        for n in range(len(player)):
            if n == 0:	# Kopf ander Farbe als der Körper
                image[player[n]["y"]][player[n]["x"]] = (255, 255, 255)
            else:
                image[player[n]["y"]][player[n]["x"]] = (255, 255, 0)
    
        sleep(speed)		#Geschwindigkeit vom Player

    # Game Over Screen
    elif gamestate == "gameover":
        gamestate_gameover(image, black, red)

    # Schicke aktuelles Bild an Lighthouse-Server
    Pyghthouse.set_image(conn, image)

    # Stelle Bild zusätzlich im Pygame-Fenster dar
    screen.clear()
    for y in range(14):
        for x in range(28):
            screen.draw.filled_rect(Rect(x*20, y*50, 20, 30), image[y][x])
            screen.draw.rect(Rect(x*20, y*50, 20, 30), (50, 50, 50))


# Verarbeite gedrückte Taste (wird bei Tastendruck aufgerufen)
def on_key_down(key):
    global gamestate, direction, fish, fishlist, player, player_len, difficulty
    # Beendet Programm, falls Escape-Taste gedrückt wurde
    if key == keys.ESCAPE and gamestate == "intro":
        Pyghthouse.close(conn)
        exit()
    # Schwierigkeitsgrad
    elif key == keys.E and gamestate == "intro":
        difficulty = "easy"
    elif key == keys.R and gamestate == "intro":
        difficulty = "hard"
    # Mit Escape-Taste kommt man zurück zum Titelbild, falls man im Spiel ist
    elif key == keys.ESCAPE and gamestate == "game":
        gamestate = "intro"
    # Mit Space-Taste kommt man ins Spiel, wenn man gerade nicht im Spiel ist, mit esc aus dem Todesscreen ins Spiel
    elif key == keys.SPACE and gamestate != "game" or key == keys.ESCAPE and gamestate == "gameover":
        gamestate = "game"
        player[0]["x"] = 14
        player[0]["y"] = 7
        direction = 0
        fishlist = []
        fish = 0
        player[1:] = []
        player_len = 1
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
    global gamestate, fish, fishlist, player, direction, player_len, danger, difficulty
    # Hard Diff delayed Death
    if difficulty == "hard" and danger == True:
        gamestate = "gameover"

    # Fish
    def fishcheck():
        global fishlist, fish
        
        while fish < fish_amount:	# erstellt so viele Fische, wie man vorher festlegt
            fish += 1
            n = {"x": random.randint(0, 27), "y": random.randint(0, 13)}	# random Koordinaten generieren
            if n in fishlist or n in player:	# neuer Fisch darf nicht auf einem anderen Fisch oder in der Schlange erscheinen
                fish -= 1
            else:
                fishlist.append(n)	# Fisch an die Liste aller Fische anhängen

    def fishmove():		# Fische können sich random bewegen
        global fishlist
        for n in range(len(fishlist)):
            if random.randint(0,10) == 1:	# nicht immer bewegen, sondern nur in 1 von 10 Fällen
                x = fishlist[n]["x"] + random.randint(-1, 1)
                if x < 0:
                    x = 27
                elif x > 27:
                    x = 0
                y = fishlist[n]["y"] + random.randint(-1, 1)
                if y < 0:
                    y = 13
                elif y > 13:
                    y = 0
                if {"x": x, "y": y} not in player and {"x": x, "y": y} not in fishlist:
                    fishlist[n] = {"x": x, "y": y}


    if gamestate == "game":
        
        # CONSUME:
        if player[0] in fishlist:
            fish -= 1
            fishlist.pop(fishlist.index(player[0]))
            sounds.chomp.play()
        fishcheck()


        if fish_move == 1:
            fishmove()

    # eine automatischer Schlangenmodus, wo sich die Schlange automatisch random bewegt:
    if automatic == 1:		
        if random.randint(0,10) == 5:
            a = random.choice(["left","right","up","down"])
            if (a == "left" and direction == "right") or (a == "right" and direction == "left") or (a == "up" and direction == "down")or (a == "down" and direction == "up"):
                pass
            else:
                direction = a

    # Bewegung der Schlange
    if direction != 0:
        head = {"x": player[0]["x"],
                "y": player[0]["y"]}  # head ist der neue Kopf, mit dem geprüft wird, was als nächstes passiert

        # Bewege Spielfigur nach links, wenn Richtung = "left":
        if direction == "left":
                head["x"] -= 1
                if head["x"] == -1 and wall_behavior == 2:
                    head["x"] = 27
        # Bewege Spielfigur nach rechts, wenn Richtung = "right":
        elif direction == "right":
                head["x"] += 1
                if head["x"] == 28 and wall_behavior == 2:
                    head["x"] = 0
        # Bewege Spielfigur nach unten, wenn Richtung = "down":
        elif direction == "down":
                head["y"] += 1
                if head["y"] == 14 and wall_behavior == 2:
                    head["y"] = 0
        # Bewegt Spielfigur nach unten, wenn Richtung = "down"
        elif direction == "up":
                head["y"] -= 1
                if head["y"] == -1 and wall_behavior == 2:
                    head["y"] = 13

        # Wenn Schlange auf Wand oder Schwanz trifft, gameover:
        if head["x"] == -1 or head["x"] == 28 or head["y"] == -1 or head["y"] == 14 or head in player[1:]:
            if difficulty == "easy":
                if danger == False:
                    danger = True
                else:
                    gamestate = "gameover"
            else:
                danger = True

        else:
            if difficulty == "easy":
                danger = False
            if head in fishlist:  # Schlange verlängern, falls man auf Fisch trifft
                player.insert(0, head)
                player_len += 1
                if player_len == 392:
                    gamestate = "win"
            else:  # Schlange bewegen, gleiche Länge
                player.insert(0, head)
                player.pop(-1)

        if gamestate == "intro" or gamestate == "gameover":
            direction = 0  # Richtung auf 0 setzen, sonst bewegt sich die Figur wieder, wenn man zurück ins Spiel geht
            danger = False


# Starte Pygame Zero
pgzrun.go()



