if __name__ == '__main__':
    first = True
    with open('d4/d4_inp.txt', 'r') as f:
        numbers_and_card = f.read()
        numbers = numbers_and_card.split('\n\n')[0].strip().split(',')
        cards = numbers_and_card.split('\n\n')[1:-1]
    rows_and_cols = []
    for card in cards:
        columns = [[], [], [], [], []]
        rows = [x.split() for x in card.split('\n')]
        for row in rows:
            for count, number in enumerate(row):
                columns[count].append(number)
        rows_and_cols.append(rows + columns)
    for number in numbers:
        new_rows_and_cols = []
        for rowcols in rows_and_cols:
            new_rewcols = []
            for rowcol in rowcols:
                if number in rowcol:
                    rowcol.remove(number)
                new_rewcols.append(rowcol)
            new_rows_and_cols.append(new_rewcols)
        rows_and_cols = new_rows_and_cols
        for i, rowcols in enumerate(rows_and_cols):
            if [] in rowcols and first:
                first = False
                non_called = set()
                for item in rowcols:
                    non_called.update(set(item))
                print('The answer to part 1 is: {}'.format(int(number)*sum([int(x) for x in non_called])))
                rows_and_cols.remove(rowcols)
            elif [] in rowcols and len(rows_and_cols) == 1:
                non_called = set()
                for item in rowcols:
                    non_called.update(set(item))
                print('The answer to part 2 is: {}'.format(int(number) * sum([int(x) for x in non_called])))
                exit()
            elif [] in rowcols:
                rows_and_cols.remove(rowcols)
