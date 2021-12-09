def find_surrounding(x, y):
    surrounding_heights = list()
    max_y = len(height_lines) - 1
    max_x = len(height_lines[0]) - 1
    surrounding = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    if x - 1 < 0:
        surrounding.remove((x - 1, y))
    if y - 1 < 0:
        surrounding.remove((x, y - 1))
    if x + 1 > max_x:
        surrounding.remove((x + 1, y))
    if y + 1 > max_y:
        surrounding.remove((x, y + 1))
    for coord in surrounding:
        surrounding_heights.append(int(height_lines[coord[1]][coord[0]]))
    return surrounding, surrounding_heights


def find_basin(current_basin, lining, size):
    new_lining = list()
    for point in lining:
        new_points = find_surrounding(point[0], point[1])[0]
        point_heights = find_surrounding(point[0], point[1])[1]
        for i, new_point in enumerate(new_points):
            if point_heights[i] < 9 and new_point not in current_basin:
                new_lining.append(new_point)
                current_basin.append(new_point)
                size += 1
    if new_lining:
        return find_basin(current_basin, new_lining, size)
    else:
        return size


if __name__ == '__main__':
    sum_risk_levels = 0
    low_points = list()
    with open('d9/d9_inp.txt') as f:
        height_lines = [x.strip() for x in f.readlines()]
    for i, line in enumerate(height_lines):
        for j, height in enumerate(line):
            if int(height) < min(find_surrounding(j, i)[1]):
                sum_risk_levels += int(height) + 1
                low_points.append((j, i))
    print('The answer to part 1 is: {}'.format(sum_risk_levels))
    basin_sizes = list()
    for item in low_points:
        basin_sizes.append(find_basin([item], [item], 1))
    basin_sizes = sorted(basin_sizes, reverse=True)
    print('The answer to part 2 is: {}'.format(basin_sizes[0]*basin_sizes[1]*basin_sizes[2]))


