from collections import defaultdict


def next_gen(old_gen, day):
    new_gen = defaultdict(lambda: 0)
    new_gen[1] = old_gen[2]
    new_gen[2] = old_gen[3]
    new_gen[3] = old_gen[4]
    new_gen[4] = old_gen[5]
    new_gen[5] = old_gen[6]
    new_gen[6] = old_gen[7] + old_gen[0]
    new_gen[7] = old_gen[8]
    new_gen[8] = old_gen[0]
    new_gen[0] = old_gen[1]
    if day == 256:
        return sum(new_gen.values())
    else:
        day += 1
        return next_gen(new_gen, day)


if __name__ == '__main__':
    current_gen = defaultdict(lambda: 0)
    with open('d6/d6_inp.txt') as f:
        lanternfish = [int(x) for x in f.read().split(',')]
    for item in lanternfish:
        current_gen[item] += 1
    print(next_gen(current_gen, 1))



