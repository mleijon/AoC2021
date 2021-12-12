import curses
import time
import os

MAX_X = int
MAX_Y = int


def find_surrounding(point):
    surrounding = list()
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (point[0] + x) in range(MAX_X) and (point[1] + y) in range(MAX_Y):
                surrounding.append((point[0] + x, point[1] + y))
            else:
                continue
    surrounding.remove(point)
    return surrounding


def increase_energy(octo):
    for x in range(MAX_X):
        for y in range(MAX_Y):
            octo[x][y] += 1
    return octo


def find_flashes(octo):
    flashes = list()
    for x in range(MAX_X):
        for y in range(MAX_Y):
            if octo[y][x] >= 10:
                flashes.append((x, y))
                octo[y][x] = 0
    return octo, flashes


def spread_flashes(octo, flash_points, flash_count):
    for flash in flash_points:
        for surr in find_surrounding(flash):
            if octo[surr[1]][surr[0]] != 0:
                octo[surr[1]][surr[0]] += 1
    octo, new_flashes = find_flashes(octo)
    if new_flashes:
        flash_count += len(new_flashes)
        return spread_flashes(octo, new_flashes, flash_count)
    else:
        return octo, flash_count


if __name__ == '__main__':
    octopuses = list()
    with open('d11_inp.txt') as f:
        for i, row in enumerate([x.strip() for x in f.readlines()]):
            octopuses.append([])
            for lvl in row:
                octopuses[i].append(int(lvl))
    MAX_X = len(octopuses[0])
    MAX_Y = len(octopuses)
    count = 0
    steps = 0
    in_sync = False
    print_flashes = False
    if input('Print flashes (y/n)?').casefold() == 'y':
        print_flashes = True
    while not in_sync:
        if print_flashes:
            curses.initscr()
            curses.curs_set(0)
            curses.start_color()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            pad = curses.newpad(11, 11)
            for item in octopuses:
                for x in item:
                    if x == 0:
                        pad.addch(str(x), curses.color_pair(1))
                    else:
                        pad.addch(str(x))
                pad.addch('\n')
            pad.refresh(0, 0, 5, 5, 20, 75)
            curses.nocbreak()
            curses.echo()
            time.sleep(0.1)
        octopuses = increase_energy(octopuses)
        octopuses, flashpoints = find_flashes(octopuses)
        octopuses, new_count = spread_flashes(octopuses, flashpoints, len(flashpoints))
        count += new_count
        if steps == 100:
            part1_answer = count
        steps += 1
        if new_count == 100:
            time.sleep(3)
            if print_flashes:
                curses.endwin()
                os.system('clear')
            print('The answer to part 1 is: {}'.format(part1_answer))
            print('The answer to part 2 is: {}'.format(steps))
            in_sync = True

