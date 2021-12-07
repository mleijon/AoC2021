if __name__ == '__main__':
    fuel_suma = 0
    fuel_sumb = 0
    with open('d7/d7_inp.txt') as f:
        hor_pos = [int(x) for x in f.read().split(',')]
    min_fuel_suma = len(hor_pos)*max(hor_pos)
    min_fuel_sumb = min_fuel_suma**2
    for align_pos in range(min(hor_pos), max(hor_pos)):
        for pos in hor_pos:
            fuel_suma += abs(align_pos - pos)
            fuel_sumb += sum([x for x in range(1, abs(align_pos - pos) + 1)])
        min_fuel_suma = min(fuel_suma, min_fuel_suma)
        min_fuel_sumb = min(fuel_sumb, min_fuel_sumb)
        fuel_suma = 0
        fuel_sumb = 0
    print('The answer to part 1 is: {}'.format(min_fuel_suma))
    print('The answer to part 2 is: {}'.format(min_fuel_sumb))

