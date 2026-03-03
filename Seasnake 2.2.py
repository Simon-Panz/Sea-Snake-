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
gamestate = "intro"	# Spielstatus zu Beginn "intro"

snake = [[{"x": 14, "y": 7}]]
direction = [0, 0]		# zu Beginn keine Richtung
snake_len = [1, 1]      # schlangelänge zu Beginn
head = [0, 0]

# Schwierigkeitsgrad:
difficulty = "easy"
danger = [False, False]

# score:
score = 0


speed = (0.25)		# Geschwindigkeit der Schlange, Verzögerung in Sekunden

level = 0

wall_behavior = 1		# 1 = Schlange stirbt bei Wand, 2 = Schlange kann durch die Wand gehen und kommt an der anderen seite wieder raus

automatic = [0, 0]		# automatischer Modus, 1 = Schlange bewegt sich von alleine

# Fish
fish = 0
fishlist = []
fish_amount = 5		# Menge an Fischen
fish_move = 1		# 1 = Fische bewegen sich, 0 = Fische bewegen sich nicht

# 2 Spieler Modus, indem man gegeneinander spielt:
player = 0
player_amount = 1		# Anzahl der Spieler



# Funktion für blauen Farbverlauf
def blue(y):
        list = (140-8*y, (155-8*y), (255-8*y))
        return list

# Zeichne Bildschirm (wird ca. 60-mal pro Sekunde aufgerufen)
def draw():
    
    global gamestate, direction, snake, speed
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    gelb = (255, 255, 102)
    lila = (255, 102, 255)

    # Zeichne aktuelles Bild
    image = Pyghthouse.empty_image()

    # ingame Darstellung:
    # intro darstellen
    if gamestate == "intro":
        gamestate_intro(image, gelb, blue)
    
    # gamestate game darstellen:
    elif gamestate == "game":
        # Hintergrund darstellen:
        for y in range(14):
            for x in range(28):
                image[y][x] = blue(y)
        # Fish färben
        for n in range(len(fishlist)):
            image[fishlist[n]["y"]][fishlist[n]["x"]] = lila
        for player in range(len(snake)):	# Schlangen aller Spieler zeichnen
            # snake färben
            for n in range(len(snake[player])):
                if n == 0:	# Kopf ander Farbe als der Körper
                    image[snake[player][n]["y"]][snake[player][n]["x"]] = white
                elif player == 0:
                    image[snake[player][n]["y"]][snake[player][n]["x"]] = gelb
                else:
                    image[snake[player][n]["y"]][snake[player][n]["x"]] = red
    
        sleep(speed)		#Geschwindigkeit vom snake
        speed = (0.25 - 0.02 * level)
        
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
    global gamestate, direction, fish, fishlist, snake, snake_len, difficulty, player_amount
    # Beendet Programm, falls Escape-Taste gedrückt wurde
    if key == keys.ESCAPE and gamestate == "intro":
        Pyghthouse.close(conn)
        exit()
    # Schwierigkeitsgrad
    elif key == keys.E and gamestate == "intro":
        difficulty = "easy"
    elif key == keys.R and gamestate == "intro":
        difficulty = "hard"
    # Anzahl der Spieler ändern durch Taste 1 oder 2:
    elif key == keys.K_1 and gamestate == "intro":
        player_amount = 1
    elif key == keys.K_2 and gamestate == "intro":
        player_amount = 2
    # 2 Spieler Modus, bei dem sich die zweite Schlange automatisch bewegt:
    elif key == keys.K_3 and gamestate == "intro":
        player_amount = 2
        automatic[1] = 1

    # Mit Escape-Taste kommt man zurück zum Titelbild, falls man im Spiel ist
    elif key == keys.ESCAPE and gamestate == "game":
        gamestate = "intro"
    # Mit Space-Taste kommt man ins Spiel, wenn man gerade nicht im Spiel ist, mit esc aus dem Todesscreen ins Spiel
    elif key == keys.SPACE and gamestate != "game" or key == keys.ESCAPE and gamestate == "gameover":
        gamestate = "game"
        
        if player_amount == 1:
            snake = [[{"x": 14, "y": 7}]]	# Schlangenbeginn für 1 Spieler Modus festlegen
        elif player_amount == 2:
            snake = [[{"x": 20, "y": 7}],[{"x": 8, "y": 7}]]	# Schlangenbeginne für 2 Spieler Modus festlegen
        direction[0] = 0
        direction[1] = 0
        fishlist = []
        fish = 0
        snake[player][1:] = []
        snake_len[player] = 1
        sounds.game_start.play()
    # Richtung nach links ändern
    elif (key == keys.LEFT) and direction[0] != "right":
             direction[0] = "left"
    # Richtung nach rechts ändern
    elif (key == keys.RIGHT) and direction[0] != "left":
             direction[0] = "right"
    # Richtung nach unten ändern
    elif (key == keys.DOWN) and direction[0] != "up":
             direction[0] = "down"
    # Richtung nach oben ändern
    elif (key == keys.UP) and direction[0] != "down":
             direction[0] = "up"
    
    # Richtung nach links ändern
    elif (key == keys.A) and direction[1] != "right":
             direction[1] = "left"
    # Richtung nach rechts ändern
    elif (key == keys.D) and direction[1] != "left":
             direction[1] = "right"
    # Richtung nach unten ändern
    elif (key == keys.S) and direction[1] != "up":
             direction[1] = "down"
    # Richtung nach oben ändern
    elif (key == keys.W) and direction[1] != "down":
             direction[1] = "up"
             
             


# Aktualisiere Spielzustand (wird ca. 60-mal pro Sekunde aufgerufen)
def update(dt):
    global gamestate, fish, fishlist, snake, direction, snake_len, danger, difficulty, score, player, head, level

    # Fish
    def fishcheck():
        global fishlist, fish
        
        while fish < fish_amount:	# erstellt so viele Fische, wie man vorher festlegt
            fish += 1
            n = {"x": random.randint(0, 27), "y": random.randint(0, 13)}	# random Koordinaten generieren
            if n in fishlist or n in snake[player]:	# neuer Fisch darf nicht auf einem anderen Fisch oder in der Schlange erscheinen
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
                # Fisch darf sich nicht in Schlange 1 oder 2 oder einen anderen Fisch bewegen
                if {"x": x, "y": y} not in snake[0] and (player_amount == 2 and {"x": x, "y": y} not in snake[1]) and {"x": x, "y": y} not in fishlist:
                    fishlist[n] = {"x": x, "y": y}


    if gamestate == "game":
        
        for player in range(len(snake)):
            
            # Hard Diff delayed Death
            if difficulty == "hard" and danger[player] == True:
                gamestate = "gameover"

                
            # CONSUME:
            if snake[player][0] in fishlist:
                fish -= 1
                fishlist.pop(fishlist.index(snake[player][0]))
                sounds.chomp.play()
                score += 1
            fishcheck()


            if fish_move == 1:
                fishmove()

            # ein automatischer Schlangenmodus, wo sich die Schlange automatisch random bewegt:
            if automatic[player] == 1:
                if random.randint(0,10) == 5:
                    a = random.choice(["left","right","up","down"])
                    if (a == "left" and direction[player] == "right") or (a == "right" and direction[player] == "left") or (a == "up" and direction[player] == "down")or (a == "down" and direction[player] == "up"):
                        pass
                    else:
                        direction[player] = a

            # Bewegung der Schlange
            if direction[player] != 0:
                head[player] = {"x": snake[player][0]["x"], "y": snake[player][0]["y"]}  # head ist der neue Kopf, mit dem geprüft wird, was als nächstes passiert

                # Bewege Spielfigur nach links, wenn Richtung = "left":
                if direction[player] == "left":
                        head[player]["x"] -= 1
                        if head[player]["x"] == -1 and wall_behavior == 2:
                            head[player]["x"] = 27
                # Bewege Spielfigur nach rechts, wenn Richtung = "right":
                elif direction[player] == "right":
                        head[player]["x"] += 1
                        if head[player]["x"] == 28 and wall_behavior == 2:
                            head[player]["x"] = 0
                # Bewege Spielfigur nach unten, wenn Richtung = "down":
                elif direction[player] == "down":
                        head[player]["y"] += 1
                        if head[player]["y"] == 14 and wall_behavior == 2:
                            head[player]["y"] = 0
                # Bewegt Spielfigur nach unten, wenn Richtung = "down"
                elif direction[player] == "up":
                        head[player]["y"] -= 1
                        if head[player]["y"] == -1 and wall_behavior == 2:
                            head[player]["y"] = 13

                # Wenn Schlange auf Wand trifft, gameover:
                if head[player]["x"] == -1 or head[player]["x"] == 28 or head[player]["y"] == -1 or head[player]["y"] == 14:
                    if difficulty == "easy":
                        if danger[player] == False:
                            danger[player] = True
                        else:
                            sounds.explosion.play()
                            gamestate = "gameover"
                            
                    else:
                        danger[player] = True

                else:
                    if difficulty == "easy":
                        danger[player] = False
                    if head[player] in fishlist:  # Schlange verlängern, falls man auf Fisch trifft
                        snake[player].insert(0, head[player])
                        snake_len[player] += 1
                         if snake_len[player] == 10:
                            level = 1
                        elif snake_len[player] == 30:
                            level = 2
                        elif snake_len[player] == 70:
                            level = 3
                        elif snake_len[player] == 120:
                            level = 4
                        elif snake_len[player] == 180:
                            level = 5
                        elif snake_len[player] == 392:
                            gamestate = "intro"
                            
                    else:  # Schlange bewegen, gleiche Länge
                        snake[player].insert(0, head[player])
                        snake[player].pop(-1)
                    # gameover wenn der Schlangenkopf den eigenen Schwanz trifft:(erst nach dem löschen des vorherigen Endes möglich)
                    if head[player] in snake[player][1:]:
                        gamestate = "gameover"

    if gamestate == "intro" or gamestate == "gameover":
        direction[player] = 0  # Richtung auf 0 setzen, sonst bewegt sich die Figur wieder, wenn man zurück ins Spiel geht
        danger = [False, False]
            level = 0


# Starte Pygame Zero
pgzrun.go()
