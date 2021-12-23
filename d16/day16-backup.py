def conv2bin(data):
    packetbin = ''
    for ch in data:
        packetbin += bin(int(ch, 16))[2:].zfill(4)
    return packetbin


if __name__ == '__main__':
    with open('d16/d16_inp.txt') as f:
        hexdata = f.readline().strip()
    packets = conv2bin(hexdata)
    p = 0
    ver_sum = 0
    header = list()
    while not set([ch for ch in packets[p:]]) in [{'0'}, {}]:
        header.append((packets[p:p + 3], packets[p + 3:p + 6]))
        packet_ver = int(header[-1][0], 2)
        ver_sum += packet_ver
        packet_type_ID = int(header[-1][1], 2)
        print('{} {}'.format(packet_ver, packet_type_ID), end='')
        p += 6

        if packet_type_ID == 4:
            nr = ''
            while int(packets[p]) == 1:
                print(' {} {}'.format(packets[p], packets[p + 1:p + 5]), end='')
                nr += packets[p + 1:p + 5]
                p += 5
            nr += packets[p + 1:p + 5]
            print(' {} {} ({})'.format(packets[p], packets[p + 1:p + 5], int(nr, 2)))
            p += 5

        elif int(packets[p]) == 0:
            print(' {} {} ({})'.format(packets[p], packets[p + 1: p + 16], int(packets[p + 1: p + 16], 2)))
            p += 16
        else:
            print(' {} {} ({})'.format(packets[p], packets[p + 1: p + 12], int(packets[p + 1: p + 12], 2)))
            p += 12
    print('The answer to part 1 is: {}'.format(ver_sum))
