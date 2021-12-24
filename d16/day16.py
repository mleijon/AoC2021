from collections import deque


def conv2bin(data):
    packetbin = ''
    for ch in data:
        packetbin += bin(int(ch, 16))[2:].zfill(4)
    return packetbin


def operation(current_packets):
    operands_used = current_packets[0][:-1]
    operands_not_used = current_packets[1]
    print(current_packets[0])
    operator = current_packets[0][-1]
    pointer = operands_used[0][2]
    op_values = []
    result = list()
    for op in operands_used:
        op_values.append(op[1])
    if operator[0] == 0:
        result = [4, sum(op_values), pointer]
    elif operator[0] == 1:
        print('I\'m here now!')
        prod = 1
        for op in operands_used:
            prod *= op[1]
        result = [4, prod, pointer]
    elif operator[0] == 2:
        result = [4, min(operands_used), pointer]
    elif operator[0] == 3:
        result = [4, max(operands_used), pointer]
    elif operator[0] == 5:
        result = [4, int(operands_used[1] > operands_used[0]), pointer]
    elif operator[0] == 6:
        result = [4, int(operands_used[1] < operands_used[0]), pointer]
    elif operator[0] == 7:
        result = [4, int(operands_used[1] == operands_used[0]), pointer]
    if operands_not_used:
        print('Operands not used: {}'.format(operands_not_used))
        print('result: {}'.format(result))
        result = deque([result])
        result.extendleft(operands_not_used)
        print('test1')
        print(result)
        return result
    else:
        print('test2')
        return result


def split_operands(pack):
    pack_used = list()
    pack_not_used = list()
    if pack[-1][3] == 0:  # length type
        for packet in pack[:-1]:
            if packet[2] <= pack[-1][2] + pack[-1][1]:
                pack_used.append(packet)
            else:
                pack_not_used.append(packet)
        pack_used.append(pack[-1])
    elif pack[-1][3] == 1:  # nr type
        pack_used = pack[-1*pack[-1][1] - 1:]
        pack_not_used = pack[:-1*pack[-1][1] - 1]
    return pack_used, pack_not_used


if __name__ == '__main__':
    with open('d16/d16_inp.txt') as f:
        hexdata = f.readline().strip()
    packets = conv2bin(hexdata)
    parsed_packets = deque()  # [operation, value, pointer, length type ID]
    p = 0
    ver_sum = 0
    header = list()
    while not set([ch for ch in packets[p:]]) in [{'0'}, {}]:
        current_packet = []
        header.append((packets[p:p + 3], packets[p + 3:p + 6]))
        packet_ver = int(header[-1][0], 2)
        ver_sum += packet_ver
        packet_type_ID = int(header[-1][1], 2)
        current_packet.append(packet_type_ID)
        p += 6
        if packet_type_ID == 4:
            nr = ''
            while int(packets[p]) == 1:
                nr += packets[p + 1:p + 5]
                p += 5
            nr += packets[p + 1:p + 5]
            current_packet.append(int(nr, 2))
            p += 5
            current_packet.append(p - 1)

        elif int(packets[p]) == 0:
            current_packet.append(int(packets[p + 1: p + 16], 2))
            p += 16
            current_packet.append(p - 1)
            current_packet.append(0)
        else:
            current_packet.append(int(packets[p + 1: p + 12], 2))
            p += 12
            current_packet.append(p - 1)
            current_packet.append(1)
        parsed_packets.appendleft(current_packet)
    print('The answer to part 1 is: {}'.format(ver_sum))
    print(parsed_packets)
    curr_select = list()
    while len(parsed_packets) > 1:
        if parsed_packets[0][0] == 4:
            curr_select.append(parsed_packets.popleft())
        else:
            curr_select.append(parsed_packets.popleft())
            parsed_packets.appendleft(operation(split_operands(curr_select)))
            curr_select = []


