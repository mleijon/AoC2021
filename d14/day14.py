def grow_pairs(pairs, current_step, final_step):
    new_pairs = list()
    for pair in pairs:
        new_pairs.append(pair[0] + conversions[pair])
        new_pairs.append(conversions[pair] + pair[1])
    current_step += 1
    if current_step == final_step:
        return new_pairs
    else:
        return grow_pairs(new_pairs, current_step, final_step)


if __name__ == '__main__':
    current_pairs = list()
    conversions = dict()
    with open('d14/d14_inp.txt') as f:
        template, steps = [x.strip() for x in f.read().split('\n\n')]
    steps = [x.split(' -> ') for x in steps.split('\n')]
    for step in steps:
        conversions[step[0]] = step[1]
    for i in range(len(template) - 1):
        current_pairs.append(template[i] + template[i + 1])
    polymer_pairs = (grow_pairs(current_pairs, 0, 40))
    polymer = polymer_pairs[0]
    for i in range(1, len(polymer_pairs) - 1):
        polymer += polymer_pairs[i][1]
    polymer += polymer_pairs[-1][1]
    elements = set([ch for ch in polymer])
    max_count = max([polymer.count(x) for x in elements])
    min_count = min([polymer.count(x) for x in elements])
    print('The answer to part 1 is: {}'.format(max_count - min_count))
