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
    with open('d13/d13_inp.txt') as f:
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
    print(current_coords)