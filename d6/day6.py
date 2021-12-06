def next_gen(old_gen, day):
    new_gen = []
    for fish in old_gen:
        if fish in [1, 2, 3, 4, 5, 6, 7, 8]:
            new_gen.append(fish - 1)
        else:
            new_gen.extend([0, 8])
    if day == 80:
        return len(new_gen)
    else:
        print('day: {}'.format(day))
        print('nr of fish: {}'.format(len(new_gen)))
        day += 1
        return next_gen(new_gen, day)


if __name__ == '__main__':
    with open('d6/d6_inp.txt') as f:
        lanternfish = [int(x) for x in f.read().split(',')]
    print(next_gen(lanternfish, 1))
