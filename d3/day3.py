def count_01(words):
    val_per_pos = []
    bit_counts = []
    word_len = len(words[0])
    for pos in range(word_len):
        val_per_pos.append([x[pos] for x in words])
        bit_counts.append((val_per_pos[pos].count('0'), val_per_pos[pos].count('1')))
    return bit_counts


def reduce_diag(words, pos, bit1, bit2):
    new_words = []
    counts = count_01(words)
    for item in words:
        if counts[pos][0] > counts[pos][1] and item[pos] == bit1:
            new_words.append(item)
        elif counts[pos][1] >= counts[pos][0] and item[pos] == bit2:
            new_words.append(item)
    words = new_words
    if (len(words) > 1) and (pos < len(words[0]) - 1):
        return reduce_diag(words, pos + 1, bit1, bit2)
    else:
        return ''.join(words[0])


if __name__ == '__main__':
    gamma = ''
    epsilon = ''
    with open('d3_inp.txt', 'r') as f:
        diag = [list(x.strip()) for x in f.readlines()]
    for bit in range(len(diag[0])):
        if count_01(diag)[bit][0] > count_01(diag)[bit][1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print('The answer to part 1 is: {}'.format(int(gamma, 2)*int(epsilon, 2)))
    oxygen_generator_rating = reduce_diag(diag, 0, '0', '1')
    c02_scrubber_rating = reduce_diag(diag, 0, '1', '0')
    print('the answer to part 2 is: {}'.format(int(oxygen_generator_rating, 2)*int(c02_scrubber_rating, 2)))
