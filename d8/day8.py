import itertools


def count_uniques():
    count = 0
    for signal in output_signals:
        if len(signal) in [2, 3, 4, 7]:
            count += 1
    print('The answer to part 1 is: {}'.format(count))


def decode_figures(figs):
    zero = set()
    one = set()
    two = set()
    three = set()
    four = set()
    five = set()
    six = set()
    seven = set()
    eight = set()
    nine = set()
    sixstrings = set()
    fivestrings = set()
    for item in figs:
        if len(item) == 2:
            one = set(list(item))
        elif len(item) == 3:
            seven = set(list(item))
        elif len(item) == 4:
            four = set(list(item))
        elif len(item) == 7:
            eight = set(list(item))
        elif len(item) == 5:
            fivestrings.add(item)
        else:
            sixstrings.add(item)
    for item in sixstrings:
        if four.issubset(set(list(item))):
            nine = set(list(item))
        elif one.issubset(set(list(item))):
            zero = set(list(item))
        else:
            six = set(list(item))
    for item in fivestrings:
        if set(list(item)).issubset(six):
            five = set(list(item))
        elif seven.issubset(set(list(item))):
            three = set(list(item))
        else:
            two = set(list(item))
    return [zero, one, two, three, four, five, six, seven, eight, nine]


if __name__ == '__main__':

    with open('d8/d8_inp.txt') as f:
        data_lines = f.readlines()
        output_signals = list(itertools.chain.from_iterable([x.split('|')[1].strip().split() for x in data_lines]))
    count_uniques()
    sum = 0
    for line in data_lines:
        figures = decode_figures(line.split('|')[0].split())
        output_number = ''
        output = line.split('|')[1].split()
        for item in output:
            for i, figure in enumerate(figures):
                if set(list(item)) == figure:
                    output_number += str(i)
        sum += int(output_number)
    print('The answer to part 2 is: {}'.format(sum))



