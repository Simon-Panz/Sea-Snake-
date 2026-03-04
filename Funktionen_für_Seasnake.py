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

    # A
    image[1][11] = blue(1)
    image[1][14] = blue(1)
    for y in range(2, 4):
        for x in range(12, 14):
            image[y][x] = blue(y)
    for y in range(5, 6):
        for x in range(12, 14):
            image[y][x] = blue(y)
    # S no. 2
    for y in range(8, 9):
        for x in range(2, 5):
            image[y][x] = blue(y)
    for y in range(10, 11):
        for x in range(1, 4):
            image[y][x] = blue(y)
    # N
    for y in range(7, 8):
        for x in range(7, 12):
            if x != 8:
                image[x][y] = blue(y)
    for y in range(8, 9):
        for x in range(7, 12):
            if x != 9:
                image[x][y] = blue(y)
    # A no. 2
    image[7][11] = blue(7)
    image[7][14] = blue(7)
    for y in range(8, 10):
        for x in range(12, 14):
            image[y][x] = blue(y)
    for y in range(11, 12):
        for x in range(12, 14):
            image[y][x] = blue(y)
    # K
    for y in range(7, 9):
        for x in range(17, 19):
            if y != 8 or x != 18:
                image[y][x] = blue(y)
    for y in range(10, 12):
        for x in range(17, 19):
            if y != 10 or x != 18:
                image[y][x] = blue(y)
    for y in range(8, 11):
        for x in range(19, 20):
            image[y][x] = blue(y)
    image[9][18]= blue(9)
    # E no. 2
    for y in range(8, 9):
        for x in range (22, 25):
            image[y][x] = blue(y)
    for y in range(10, 11):
        for x in range (22, 25):
            image[y][x] = blue(y)
    
    
def gamestate_gameover(image, black, red):
# schwarzes Bild, welches dann eingefärbt wird:
    for y in range(14):
        for x in range(28):
            image[y][x] = black
    # rote Bereiche für Schrift
    for y in range(2, 7):
        for x in range(3, 25):
            image[y][x] = red
    for y in range(8, 13):
        for x in range(3, 25):
            image[y][x] = red
    # Buchstaben einfärben:
    # "GAME" einfärben:
    # G:
    image[2][3] = black
    image[6][3] = black
    image[5][6] = black
    image[5][5] = black
    for y in range(3, 6):
        image[y][4] = black
    for x in range(5, 8):
        image[3][x] = black
    for y in range(2, 7):
        image[y][8] = black
    # A:
    image[2][9] = black
    image[2][12] = black
    for y in range(2, 7):
        image[y][13] = black
    for x in range(10, 12):
        image[3][x] = black
    for x in range(10, 12):
        image[5][x] = black
    for x in range(10, 12):
        image[6][x] = black
    # M:
    for y in range(2, 7):
        image[y][19] = black
    for x in range(15, 18):
        image[2][x] = black
        image[3][16] = black
    for y in range(4, 7):
        image[y][15] = black
    for y in range(4, 7):
        image[y][17] = black
    for y in range(5, 7):
        image[y][16] = black
    # E:
    for x in range(21, 25):
        image[3][x] = black
    for x in range(21, 25):
        image[5][x] = black
    # "OVER" einfärben:
    # O:
    image[8][3] = black
    image[8][7] = black
    image[12][3] = black
    image[12][7] = black
    for y in range(8, 13):
        image[y][8] = black
    for x in range(4, 7):
        for y in range(9, 12):
            image[y][x] = black
    # V:
    for y in range(11, 13):
        image[y][9] = black
    for y in range(11, 13):
        image[y][13] = black
    for y in range(8, 11):
        image[y][10] = black
    for y in range(8, 11):
        image[y][12] = black
    for y in range(8, 12):
        image[y][11] = black
    for y in range(8, 13):
        image[y][14] = black
    image[12][10] = black
    image[12][12] = black
    # E:
    for x in range(16, 20):
        image[9][x] = black
    for x in range(16, 20):
        image[11][x] = black
    for y in range(8, 13):
        image[y][20] = black
    # R:
    for x in range(22, 24):
        image[9][x] = black
    for x in range(24, 26):
        image[8][x] = black
    for y in range(11, 13):
        image[y][22] = black
    image[12][23] = black
    for y in range(10, 12):
        image[y][24] = black
