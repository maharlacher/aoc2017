# daythree3_spiral

def enum(**enums):
    return type('Enum', (), enums)

DIRECTION = enum(UP = 1, LEFT = 2, DOWN = 3, RIGHT = 4)

w, h = 602, 602;
spiral = [[0 for x in range(w)] for y in range(h)]

spiral[300][300] = 1
spiral[301][300] = 2

x = 301
y = 300
Heading = DIRECTION.UP

for next_num in range(325489-2):
    if (Heading == DIRECTION.UP):
        if (spiral[x-1][y] == 0):
            Heading = DIRECTION.LEFT
            x = x - 1
        else:
            y = y + 1
    elif (Heading == DIRECTION.LEFT):
        if (spiral[x][y-1] == 0):
            Heading = DIRECTION.DOWN
            y = y - 1
        else:
            x = x - 1
    elif (Heading == DIRECTION.DOWN):
        if (spiral[x+1][y] == 0):
            Heading = DIRECTION.RIGHT
            x = x + 1
        else:
            y = y - 1
    else:
        if (spiral[x][y+1] == 0):
            Heading = DIRECTION.UP
            y = y + 1
        else:
            x = x + 1

    spiral[x][y] = next_num + 3

print x,y,Heading,next_num+3
print(x-300,y-300,(x-300)+(y-300))
