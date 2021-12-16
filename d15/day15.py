def make_steps(positions, cavern, steps):  # positions [((x, y), risk)]
    width = len(cavern[0])
    new_positions = list()
    for pos in positions:
        for step in steps:
            new_position = tuple(sum(x) for x in zip(pos[0], step))
            in_frame = max(new_position) < width and min(new_position) >= 0
            if in_frame:
                new_risk = pos[1] + cavern[new_position[1]][new_position[0]]
                allowed_risk = new_risk < risk_matrix[new_position[1]][new_position[0]]
                if allowed_risk:
                    risk_matrix[new_position[1]][new_position[0]] = new_risk
                    if [x for x in new_positions if x[0] == new_position and x[1] > new_risk]:
                        new_positions.remove([x for x in new_positions if x[0]
                                              == new_position][0])
                        new_positions.append((new_position, new_risk))
                    elif not [x for x in new_positions if x[0] == new_position]:
                        new_positions.append((new_position, new_risk))
    return new_positions


def make_large_cavern(cave):
    import copy
    width = len(cave[0])
    lcave = copy.deepcopy(cave)
    for r in range(width):
        for c in range(width, 5 * width):
            new_risk = lcave[r][c - width] + 1
            if new_risk == 10:
                new_risk = 1
            lcave[r].append(new_risk)
    for r in range(width, 5 * width):
        new_row = []
        for c in range(5 * width):
            new_risk = lcave[r - width][c] + 1
            if new_risk == 10:
                new_risk = 1
            new_row.append(new_risk)
        lcave.append(new_row)
    return lcave


def make_risk_mtx(cavern):
    dim = len(cavern[0])
    sum_elem = 0
    risk_mtx = list()
    for row in range(dim):
        for col in range(dim):
            sum_elem += cavern[row][col]
    for row in range(dim):
        risk_mtx.append([])
        for col in range(dim):
            risk_mtx[row].append(sum_elem)
    return risk_mtx


if __name__ == '__main__':
    small_cavern = list()
    large_cavern = list()
    risk_matrix = list()
    with open('d15/simon.txt') as f:
        cavern_rows = [x.strip() for x in f.readlines()]
        for i, row in enumerate(cavern_rows):
            small_cavern.append([])
            for ch in row:
                small_cavern[i].append(int(ch))
    risk_matrix = make_risk_mtx(small_cavern)
    new_positions = [((0, 0), 0)]
    while new_positions:
        new_positions = make_steps(new_positions, small_cavern, [(0, 1), (1, 0), (-1, 0), (0, -1)])
    lowest_risk = risk_matrix[len(small_cavern) - 1][len(small_cavern) - 1]
    print('The answer to part 1 is: {}'.format(lowest_risk))
    large_cavern = make_large_cavern(small_cavern)
    risk_matrix = make_risk_mtx(large_cavern)
    new_positions = [((0, 0), 0)]
    while new_positions:
        new_positions = make_steps(new_positions, large_cavern, [(0, 1), (1, 0), (-1, 0), (0, -1)])
    lowest_risk = risk_matrix[len(large_cavern) - 1][len(large_cavern) - 1]
    print('The answer to part 2 is: {}'.format(lowest_risk))

