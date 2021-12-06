if __name__ == '__main__':
    vents = list()
    count = 0
    with open('d5/d5_inp.txt') as f:
        for line in [x.strip().split(' -> ') for x in f.readlines()]:
            start = (int(line[0].split(',')[0]), int(line[0].split(',')[1]))
            end = (int(line[1].split(',')[0]), int(line[1].split(',')[1]))
            if start[0] == end[0]:
                for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    vents.append((start[0], i))
            elif start[1] == end[1]:
                for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    vents.append((i, start[1]))
        for item in set(vents):
            if vents.count(item) > 1:
                count += 1
        print('The answer to part 1 is: {}'.format(count))

