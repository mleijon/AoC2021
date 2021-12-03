if __name__ == '__main__':
    gamma = ''
    epsilon = ''
    with open('d3_inp.txt', 'r') as f:
        diag = [list(x.strip()) for x in f.readlines()]
    val_per_pos = [[]] * len(diag[0])
    for pos in range(len(diag[0])):
        val_per_pos[pos].append([x[pos] for x in diag])
        count_0 = val_per_pos[0][pos].count('0')
        count_1 = val_per_pos[0][pos].count('1')
        if count_0 > count_1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print('The answer to part 1 is: {}'.format(int(gamma, 2)*int(epsilon, 2)))



