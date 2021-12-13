import curses
import time


def turn(axis, coords):
    new_coords = set()
    for coord in coords:
        if axis[0] == 'x':
            if coord[0] <= axis[1]:
                new_coords.add(coord)
            else:
                new_coords.add((2*axis[1] - coord[0], coord[1]))
        if axis[0] == 'y':
            if coord[1] <= axis[1]:
                new_coords.add(coord)
            else:
                new_coords.add((coord[0], 2 * axis[1] - coord[1]))
    return new_coords


if __name__ == '__main__':
    with open('d13_inp.txt') as f:
        coordinates, folds = f.read().split('\n\n')
        start_coordinates = [(int(x[0]), int(x[1])) for x in [s.split(',') for s in coordinates.split('\n')]]
        folds = [(x[0][11:], int(x[1])) for x in [s.split('=') for s in folds.strip().split('\n')]]
    current_coords = start_coordinates
    used_folds = folds[:1]
    for fold in used_folds:
        current_coords = turn(fold, current_coords)
    print('The answer to part 1 is: {}'.format(len(current_coords)))
    current_coords = start_coordinates
    used_folds = folds[:1]
    for fold in folds:
        current_coords = turn(fold, current_coords)
    max_x = max([s[0] for s in current_coords])
    max_y = max([s[1] for s in current_coords])
    curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    pad = curses.newpad(50, 50)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in current_coords:
                time.sleep(0.1)
                pad.addch(' ', curses.color_pair(1))
                pad.refresh(0, 0, 5, 5, 20, 75)
            else:
                time.sleep(0.1)
                pad.addch(' ')
                pad.refresh(0, 0, 5, 5, 20, 75)
        pad.addch('\n')
    pad.refresh(0, 0, 5, 5, 20, 75)
    curses.nocbreak()
    curses.echo()
    time.sleep(10)
    curses.endwin()

