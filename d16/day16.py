def conv2bin(p):
    packetbin = ''
    for ch in p:
        packetbin += bin(int(ch, 16))[2:].zfill(4)
    return packetbin


def read_lit(p):
    bit = 1
    pointer
    while bit == 1:



def read_len_type_0(p):
    return p


def read_len_type_1(p):
    return p


def read_ver_and_type(p):
    v = int(bin_packet[pointer:pointer + 3], 2)
    t = int(bin_packet[pointer + 3:pointer + 6], 2)
    return v, t


if __name__ == '__main__':
    ver_sum = 0
    with open('d16/test.txt') as f:
        packets = f.readline().strip()
    bin_packet = conv2bin(packets)
    print(bin_packet)
    pointer = 0
    while pointer < len(bin_packet):
        ver, typ = read_ver_and_type(pointer)
        ver_sum += ver
        if typ == 4:
            pointer += 6
            pointer = read_lit(pointer)
        elif bin_packet[pointer + 6] == 0:
            pointer += 7
            pointer = read_len_type_0(pointer)
        elif bin_packet[pointer + 6] == 1:
            pointer += 7
            pointer = read_len_type_0(pointer)

