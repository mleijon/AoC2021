def p1(m):
    vert_dist = sum([move * (direction == 'down') - move * (direction == 'up') for (move, direction) in m])
    hori_dist = sum([move * (direction == 'forward') for (move, direction) in m])
    return vert_dist*hori_dist


def p2(m):
    aim = 0
    vert_dist = 0
    hori_dist = 0
    for move in m:
        if move[1] == 'up':
            aim -= move[0]
        elif move[1] == 'down':
            aim += move[0]
        else:
            hori_dist += move[0]
            vert_dist += aim*move[0]
    return vert_dist*hori_dist


if __name__ == '__main__':
    with open('d2_inp.txt', 'r') as f:
        moves = [(int(m.split()[1]), m.split()[0].strip()) for m in f.readlines()]
    print('The answer to part 1 is: {}'.format(p1(moves)))
    print('THe answer to part 2 is: {}'.format(p2(moves)))

