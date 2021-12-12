from collections import defaultdict


def invalid_cave(cave_path, new_cave, part):
    if part == '1':
        if new_cave in cave_path and new_cave.islower():
            return True
    if part == '2':
        if new_cave == 'start':
            return True
        elif new_cave.isupper() or new_cave not in cave_path:
            return False
        elif cave_path.count(new_cave) > 1:
            return True
        else:
            for cave in cave_path:
                if cave.islower() and cave_path.count(cave) == 2:
                    return True
            else:
                return False


def build_paths(current_paths, path_count, part):
    new_paths = list()
    for path in current_paths:
        connecting_caves = connections[path[-1]]
        for cave in connecting_caves:
            new_path = path.copy()
            if cave == 'end':
                path_count += 1
                continue
            elif invalid_cave(path, cave, part):
                continue
            else:
                new_path.append(cave)
            new_paths.append(new_path)
    if not new_paths:
        return path_count
    else:
        return build_paths(new_paths, path_count, part)


if __name__ == '__main__':
    path_start = [['start']]
    cave_set = set()
    connections = defaultdict(lambda: [])
    with open('d12/d12_inp.txt') as f:
        single_connects = [x.strip() for x in f.readlines()]
    for connect in [x.split('-') for x in single_connects]:
        cave_set.update(connect)
    for cave in cave_set:
        for connect in single_connects:
            if cave in connect.split('-'):
                connecting_cave = connect.split('-')
                connecting_cave.remove(cave)
                connections[cave] += connecting_cave
    part = '1'
    print('the answer to part 1 is: {}'.format(build_paths(path_start, 0, part)))
    part = '2'
    print('the answer to part 2 is: {}'.format(build_paths(path_start, 0, part)))

