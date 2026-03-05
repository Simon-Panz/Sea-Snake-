# Startbildschirm zeichnen
def gamestate_intro(image, farbe1, farbe2):
    # blauer Verlauf
    for y in range(14):
        for x in range(28):
            image[y][x] = farbe2(y)

    # schwarzer Bereich
    for y in range(1, 12):
        for x in range(1, 26):
            image[y][x] = farbe1
    for y in range(1, 6):
            for x in range(16, 26):
                image[y][x] = farbe2(y)
    # Striche zwischen Buchstaben
    for x in range(28):
        if x % 5 == 0:
            for y in range(1, 12):
                image[y][x] = farbe2(y)
    # Strich zwischen Zeilen
    for y in range (6, 7):
        for x in range(1, 27):
            image[y][x] = farbe2(y)
    # S
    for y in range(2, 3):
        for x in range(2, 5):
            image[y][x] = farbe2(y)
    for y in range(4, 5):
        for x in range(1, 4):
            image[y][x] = farbe2(y)
    # E
    for y in range(2, 3):
        for x in range(7, 10):
            image[y][x] = farbe2(y)
    for y in range(4, 5):
        for x in range(7, 10):
            image[y][x] = farbe2(y)
    # A
    image[1][11] = farbe2(1)
    image[1][14] = farbe2(1)
    for y in range(2, 4):
        for x in range(12, 14):
            image[y][x] = farbe2(y)
    for y in range(5, 6):
        for x in range(12, 14):
            image[y][x] = farbe2(y)
    # S no. 2
    for y in range(8, 9):
        for x in range(2, 5):
            image[y][x] = farbe2(y)
    for y in range(10, 11):
        for x in range(1, 4):
            image[y][x] = farbe2(y)
    # N
    for y in range(7, 8):
        for x in range(7, 12):
            if x != 8:
                image[x][y] = farbe2(y)
    for y in range(8, 9):
        for x in range(7, 12):
            if x != 9:
                image[x][y] = farbe2(y)
    # A no. 2
    image[7][11] = farbe2(7)
    image[7][14] = farbe2(7)
    for y in range(8, 10):
        for x in range(12, 14):
            image[y][x] = farbe2(y)
    for y in range(11, 12):
        for x in range(12, 14):
            image[y][x] = farbe2(y)
    # K
    for y in range(7, 9):
        for x in range(17, 19):
            if y != 8 or x != 18:
                image[y][x] = farbe2(y)
    for y in range(10, 12):
        for x in range(17, 19):
            if y != 10 or x != 18:
                image[y][x] = farbe2(y)
    for y in range(8, 11):
        for x in range(19, 20):
            image[y][x] = farbe2(y)
    image[9][18]= farbe2(9)
    # E no. 2
    for y in range(8, 9):
        for x in range (22, 25):
            image[y][x] = farbe2(y)
    for y in range(10, 11):
        for x in range (22, 25):
            image[y][x] = farbe2(y)
    
# Gameover Screen zeichnen:
def gamestate_gameover(image, farbe1, farbe2):
# schwarzes Bild, welches dann eingefärbt wird:
    for y in range(14):
        for x in range(28):
            image[y][x] = farbe1
    # rote Bereiche für Schrift
    for y in range(2, 7):
        for x in range(3, 25):
            image[y][x] = farbe2
    for y in range(8, 13):
        for x in range(3, 25):
            image[y][x] = farbe2
    # Buchstaben einfärben:
    # "GAME" einfärben:
    # G:
    image[2][3] = farbe1
    image[6][3] = farbe1
    image[5][6] = farbe1
    image[5][5] = farbe1
    for y in range(3, 6):
        image[y][4] = farbe1
    for x in range(5, 8):
        image[3][x] = farbe1
    for y in range(2, 7):
        image[y][8] = farbe1
    # A:
    image[2][9] = farbe1
    image[2][12] = farbe1
    for y in range(2, 7):
        image[y][13] = farbe1
    for x in range(10, 12):
        image[3][x] = farbe1
    for x in range(10, 12):
        image[5][x] = farbe1
    for x in range(10, 12):
        image[6][x] = farbe1
    # M:
    for y in range(2, 7):
        image[y][19] = farbe1
    for x in range(15, 18):
        image[2][x] = farbe1
        image[3][16] = farbe1
    for y in range(4, 7):
        image[y][15] = farbe1
    for y in range(4, 7):
        image[y][17] = farbe1
    for y in range(5, 7):
        image[y][16] = farbe1
    # E:
    for x in range(21, 25):
        image[3][x] = farbe1
    for x in range(21, 25):
        image[5][x] = farbe1
    # "OVER" einfärben:
    # O:
    image[8][3] = farbe1
    image[8][7] = farbe1
    image[12][3] = farbe1
    image[12][7] = farbe1
    for y in range(8, 13):
        image[y][8] = farbe1
    for x in range(4, 7):
        for y in range(9, 12):
            image[y][x] = farbe1
    # V:
    for y in range(11, 13):
        image[y][9] = farbe1
    for y in range(11, 13):
        image[y][13] = farbe1
    for y in range(8, 11):
        image[y][10] = farbe1
    for y in range(8, 11):
        image[y][12] = farbe1
    for y in range(8, 12):
        image[y][11] = farbe1
    for y in range(8, 13):
        image[y][14] = farbe1
    image[12][10] = farbe1
    image[12][12] = farbe1
    # E:
    for x in range(16, 20):
        image[9][x] = farbe1
    for x in range(16, 20):
        image[11][x] = farbe1
    for y in range(8, 13):
        image[y][20] = farbe1
    # R:
    for x in range(22, 24):
        image[9][x] = farbe1
    for x in range(24, 26):
        image[8][x] = farbe1
    for y in range(11, 13):
        image[y][22] = farbe1
    image[12][23] = farbe1
    for y in range(10, 12):
        image[y][24] = farbe1



# Score-Screen zeichnen:
# alle Zahlen festlegen (3 mal 5 Größe):
digits = {
    "0": [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(2,2),(0,3),(2,3),(0,4),(1,4),(2,4)],
    "1": [(1,0),(1,1),(1,2),(1,3),(1,4)],
    "2": [(0,0),(1,0),(2,0),(2,1),(0,2),(1,2),(2,2),(0,3),(0,4),(1,4),(2,4)],
    "3": [(0,0),(1,0),(2,0),(2,1),(1,2),(2,2),(2,3),(0,4),(1,4),(2,4)],
    "4": [(0,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2),(2,3),(2,4)],
    "5": [(0,0),(1,0),(2,0),(0,1),(0,2),(1,2),(2,2),(2,3),(0,4),(1,4),(2,4)],
    "6": [(1,0),(2,0),(0,1),(0,2),(1,2),(2,2),(0,3),(2,3),(0,4),(1,4),(2,4)],
    "7": [(0,0),(1,0),(2,0),(2,1),(1,2),(1,3),(1,4)],
    "8": [(0,0),(1,0),(2,0),(0,1),(2,1),(1,2),(0,3),(2,3),(0,4),(1,4),(2,4)],
    "9": [(0,0),(1,0),(2,0),(0,1),(2,1),(1,2),(2,2),(2,3),(0,4),(1,4)],
    ":": [(1,1),(1,3)],
    "!": [(1,0),(1,1),(1,2),(1,4)]
}

# Funktion, um den score zu zeichnen:
def gamestate_score(image, score, player_amount, winner):
    gold = (255, 215, 0)
    grün = (102, 255, 51)
    
    for player in range(player_amount):
        text = str(player+1)+":"+str(score[player])	# Score in einen string umwandeln
        if player == 0 and winner == "player1":
            text = text + "!"
        elif player == 1 and winner == "player2":
            text = text + "!"
        

        # Breite des Scores berechnen (jede Ziffer 3 Pixel + 1 Pixel Abstand)
        text_width = len(text) * 4 - 1		# letzte Ziffer im Score hat braucht keine Leerreihe am Ende
        
        text_height = 5 + (player_amount - 1) * 6

        # Startpunkt bestimmen:
        start_x = (28 - text_width) // 2
        start_y = (14 - text_height) // 2

        # Jede Ziffer zeichnen
        for index in range(len(text)):
            digit = text[index]
            if digit in digits:
                if digit == ":" or digit == "!" or index == 0:
                    farbe = grün
                else: farbe = gold
                # Pixel der Ziffer setzen
                for i in range(len(digits[digit])):
                    digit_x = digits[digit][i][0]
                    digit_y = digits[digit][i][1]
                    x = start_x + digit_x + index * 4
                    y = start_y + digit_y + player * 6
                    if 0 <= x < 28 and 0 <= y < 14:
                        image[y][x] = farbe
