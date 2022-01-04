XMIN = 102
XMAX = 157
YMIN = -146
YMAX = -90


def calc_trajectory(x, y, vx, vy):
    x_new = x + vx - (vx > 0) + (vx < 0)
    y_new = y + vy - 1
    vx_new = vx - (vx > 0) + (vx < 0)
    vy_new = vy - 1
    return x_new, y_new, vx_new, vy_new


if __name__ == '__main__':
    x = 0
    y = 0
    vx0 = 1
    vy0 = -200
    vx = vx0
    vy = vy0
    y_topp = YMIN
    y_topp_old = YMIN
    vy_max = 10000
    vx0_max = 2000
    count = 0
    while vx0 <= vx0_max:
        while vy <= vy_max:
            if y > y_topp:
                y_topp = y
            x, y, vx, vy = calc_trajectory(x, y, vx, vy)
            if XMIN <= x <= XMAX and YMIN <= y <= YMAX:
                x = 0
                y = 0
                vy0 += 1
                vx = vx0
                vy = vy0
                y_topp_old = y_topp
                count += 1
            elif x > XMAX or y < YMIN:
                x = 0
                y = 0
                vy0 += 1
                vx = vx0
                vy = vy0
                y_topp = y_topp_old
        vx0 += 1
        x = 0
        y = 0
        vy0 = -200
        vy = vy0
    print('The answer t0 part 1 is: {}'.format(y_topp))
    print('The answer t0 part 2 is: {}'.format(count))



