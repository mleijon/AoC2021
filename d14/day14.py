from collections import defaultdict


def grow_pairs(previous_pairs, current_step, final_step):
    new_pairs = defaultdict(lambda: 0)
    for pair in previous_pairs.keys():
        new_pairs[pair[0] + conversions[pair]] += previous_pairs[pair]
        new_pairs[conversions[pair] + pair[1]] += previous_pairs[pair]
    current_step += 1
    if current_step == final_step:
        elements = set()
        element_count = defaultdict(lambda: 0)
        for item in [{x[0], x[1]} for x in new_pairs.keys()]:
            elements.update(item)
        for element in elements:
            for pair in new_pairs.keys():
                if element in pair:
                    element_count[element] += new_pairs[pair] * pair.count(element)
        for element in element_count.keys():
            if element_count[element] % 2 != 0:
                element_count[element] = (element_count[element] - 1) // 2 + 1
            else:
                element_count[element] = (element_count[element]) // 2
        return element_count
    else:
        return grow_pairs(new_pairs, current_step, final_step)


def calc_diff(current_pairs, steps):
    pair_counts = grow_pairs(current_pairs, 0, steps)
    max_count = max([x for x in pair_counts.values()])
    min_count = min([x for x in pair_counts.values()])
    return max_count - min_count


if __name__ == '__main__':
    current_pairs = defaultdict(lambda: 0)
    conversions = dict()
    elements = set()
    element_count = defaultdict(lambda: 0)
    with open('d14/d14_inp.txt') as f:
        template, steps = [x.strip() for x in f.read().split('\n\n')]
    first_element = template[0]
    last_element = template[-1]
    steps = [x.split(' -> ') for x in steps.split('\n')]
    for step in steps:
        conversions[step[0]] = step[1]
    for i in range(len(template) - 1):
        current_pairs[template[i] + template[i + 1]] += 1
    print('The answer to part 1 is: {}'.format(calc_diff(current_pairs, 10)))
    print('The answer to part 2 is: {}'.format(calc_diff(current_pairs, 40)))


