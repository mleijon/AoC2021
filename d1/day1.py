def mov_av(data, win):
    mov_av_data = []
    for i in range(len(data)):
        if i + win <= len(data):
            s = 0
            for j in range(i, i + win):
                s += data[j]
            mov_av_data.append(s)
    return mov_av_data


def calc_inc(dep, window):
    increased = 0
    movav = mov_av(dep, window)
    current_depth = movav[0]
    for i in range(1, len(movav)):
        if movav[i] > current_depth:
            increased += 1
        current_depth = movav[i]
    return increased


if __name__ == '__main__':
    with open('d1/d1_inp.txt', 'r') as f:
        depths = [int(d.strip()) for d in f.readlines()]
    print('The answer to part 1 is: {}'.format(calc_inc(depths, 1)))
    print('The answer to part 2 is: {}'.format(calc_inc(depths, 3)))
