def conv2bin(p):
    packetbin = ''
    for ch in p:
        packetbin += bin(int(ch, 16))[2:].zfill(4)
    return packetbin


if __name__ == '__main__':
    with open('d16/d16_inp.txt') as f:
        packets = f.readline().strip()
    print(conv2bin(packets))