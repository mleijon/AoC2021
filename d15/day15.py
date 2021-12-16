def make_steps(positions, cavern):  # positions [((x, y), risk)]
    width = len(cavern[0])
    new_positions = list()
    new_positions_red = list()
    for pos in positions:
        for step in ((1, 0), (0, 1)):
            new_position = tuple(sum(x) for x in zip(pos[0], step))
            if max(new_position) < width:
                new_risk = pos[1] + cavern[new_position[1]][new_position[0]]
                if new_position == (width - 1, width - 1):
                    final_paths.append(new_risk)
                else:
                    new_positions.append((new_position, new_risk))
    new_positions_set = set([x[0] for x in new_positions])
    for item in new_positions_set:
        pos_minrisk = min([x[1] for x in new_positions if x[0] == item])
        new_positions_red.append((item, pos_minrisk))
    new_positions = new_positions_red
    return new_positions


def make_large_cavern(cave):
    width = len(cave[0])
    lcave = cave
    for r in range(width):
        for c in range(width, 5*width):
            new_risk = lcave[r][c - width] + 1
            if new_risk == 10:
                new_risk = 1
            lcave[r].append(new_risk)
    for r in range(width, 5*width):
        new_row = []
        for c in range(5*width):
            new_risk = lcave[r - width][c] + 1
            if new_risk == 10:
                new_risk = 1
            new_row.append(new_risk)
        lcave.append(new_row)
    return lcave


if __name__ == '__main__':
    small_cavern = list()
    large_cavern = list()
    final_paths = list()
    with open('d15/d15_inp.txt') as f:
        cavern_rows = [x.strip() for x in f.readlines()]
        for i, row in enumerate(cavern_rows):
            small_cavern.append([])
            for ch in row:
                small_cavern[i].append(int(ch))
    current_positions = [((0, 0), 0)]
    while current_positions:
        current_positions = make_steps(current_positions, small_cavern)
    print('The answer to part 1 is: {}'.format(min(final_paths)))
    large_cavern = make_large_cavern(small_cavern)
    current_positions = [((0, 0), 0)]
    final_paths = []
    while current_positions:
        current_positions = make_steps(current_positions, large_cavern)
    print('The answer to part 2 is: {}'.format(min(final_paths)))
