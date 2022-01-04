def conv2bin(data) -> str:
    packetbin = ''
    for ch in data:
        packetbin += bin(int(ch, 16))[2:].zfill(4)
    return packetbin


def find_calculable(current_packets) -> tuple:

    def can_compute() -> tuple:
        if pkt[3] == 0:
            i = 1
            try:
                while (current_packets[pkt_nr + i][2] <= (current_packets[pkt_nr][2] + current_packets[pkt_nr][1])) \
                        and current_packets[pkt_nr + i][0] == 4:
                    if current_packets[pkt_nr + i][2] == current_packets[pkt_nr][1] + current_packets[pkt_nr][2]:
                        return pkt_nr, pkt_nr + i
                    else:
                        i += 1
            except IndexError:
                return ()
        elif pkt[3] == 1:
            for i in range(pkt_nr + 1, pkt_nr + current_packets[pkt_nr][1] + 1):
                if current_packets[i][0] == 4:
                    continue
                else:
                    return ()
            return pkt_nr, pkt_nr + current_packets[pkt_nr][1]

    for pkt_nr, pkt in enumerate(current_packets):
        if len(pkt) == 4:
            if can_compute():
                return can_compute()
            else:
                continue

        
def compute(current_packets, calc_pack) -> list:
    calc_pack = current_packets[calc_pack[0]:calc_pack[1] + 1]
    operator = calc_pack[0][0]
    new_pointer = calc_pack[-1][2]
    if operator == 0:
        new_value = sum([x[1] for x in calc_pack[1:]])
    elif operator == 1:
        new_value = 1
        for op in calc_pack[1:]:
            new_value *= op[1]
    elif operator == 2:
        new_value = min([x[1] for x in calc_pack[1:]])
    elif operator == 3:
        new_value = max([x[1] for x in calc_pack[1:]])
    elif operator == 5:
        new_value = int(calc_pack[1][1] > calc_pack[2][1])
    elif operator == 6:
        new_value = int(calc_pack[1][1] < calc_pack[2][1])
    else:
        new_value = int(calc_pack[1][1] == calc_pack[2][1])
    return [4, new_value, new_pointer]


if __name__ == '__main__':
    with open('d16/d16_inp.txt') as f:
        hexdata = f.readline().strip()
    packets = conv2bin(hexdata)
    parsed_packets = list()  # [operation, value, pointer, length type ID]
    p = 0
    ver_sum = 0
    header = list()
    while not set([ch for ch in packets[p:]]) in [{'0'}, set()]:
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
        parsed_packets.append(current_packet)
    print('The answer to part 1 is: {}'.format(ver_sum))
    while len(parsed_packets) > 1:
        subpkt = find_calculable(parsed_packets)
        parsed_pkt_new = parsed_packets[:subpkt[0]]
        parsed_calc = compute(parsed_packets, find_calculable(parsed_packets))
        parsed_pkt_end = parsed_packets[subpkt[1] + 1:]
        parsed_pkt_new.append(parsed_calc)
        parsed_pkt_new.extend(parsed_pkt_end)
        parsed_packets = parsed_pkt_new.copy()
    print('The answer to part 2 is: {}'.format(parsed_packets[0][1]))
