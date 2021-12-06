def create_path(st, en):
    path = [st]
    pos_x = st[0]
    pos_y = st[1]
    nr_steps = max(abs(st[0] - en[0]), abs(st[1] - en[1]))
    if st[0] < en[0]:
        dir_x = 1
    elif st[0] > en[0]:
        dir_x = -1
    else:
        dir_x = 0
    if st[1] < en[1]:
        dir_y = 1
    elif st[1] > en[1]:
        dir_y = -1
    else:
        dir_y = 0
    for _ in range(1, nr_steps):
        pos_x += dir_x
        pos_y += dir_y
        path.append((pos_x, pos_y))
    path.append(en)
    return path


if __name__ == '__main__':
    all_vents = set()
    high_vents = set()
    all_vents_a = set()
    high_vents_a = set()
    with open('d5/d5_inp.txt') as f:
        for line in [x.strip().split(' -> ') for x in f.readlines()]:
            start = (int(line[0].split(',')[0]), int(line[0].split(',')[1]))
            end = (int(line[1].split(',')[0]), int(line[1].split(',')[1]))
            for position in create_path(start, end):
                if position in all_vents:
                    high_vents.add(position)
                all_vents.add(position)
                if start[0] == end[0] or start[1] == end[1]:
                    if position in all_vents_a:
                        high_vents_a.add(position)
                    all_vents_a.add(position)
        print('The answer to part 1 is: {}'.format(len(high_vents_a)))
        print('The answer to part 2 is: {}'.format(len(high_vents)))