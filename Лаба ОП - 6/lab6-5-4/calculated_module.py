def distance(Xp, Yp, Xo, Yo):
    d_x = (Xp - Xo) ** 2
    d_y = (Yp - Yo) ** 2

    return (d_x + d_y) ** 0.5


def points(Xo, Yo, R):
    counter = 0
    for X in range(int(Xo - R - 2), int(Xo + R + 2)):
        for Y in range(int(Yo - R - 2), int(Yo + R + 2)):
            if distance(X, Y, Xo, Yo) <= R:
                counter += 1
    return counter