def diamond_square(arr, lenght) :
    h = lenght
    t[0][0] = 0
    t[0][h - 1] = 0
    t[h - 1][h - 1] = 0
    t[h - 1][0] = 0
    i = h - 1

    while i > 1 :
        id = i / 2
        
        x = id
        while x < h :
            y = id
            while y < h :
                moy = ( t[x - id][y - id] + t[x - id][y + id] + t[x + id][y + id] + t[x + id][y - id] ) / 4
                t[x][y] = moy + 0#random
                y += i
            x += i