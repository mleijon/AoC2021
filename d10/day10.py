from collections import defaultdict


def auto_comp_score(par_string):
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    total_score = 0
    for par in par_string[::-1]:
        total_score *= 5
        total_score += scores[par]
    return total_score


if __name__ == '__main__':
    par = {'{': '}', '[': ']', '(': ')', '<': '>'}
    counter = defaultdict(lambda: 0)
    incomplete = list()
    with open('d10/d10_inp.txt') as f:
        chunk_rows = [x.strip() for x in f.readlines()]
    for chunk_row in chunk_rows:
        correct = True
        check = ''
        for char in chunk_row:
            if char in par.keys():
                check += char
            elif par[check[-1]] == char:
                check = check[:-1]
            else:
                counter[char] += 1
                correct = False
                break
        if correct:
            incomplete.append(check)
    syntax_error_score = counter[')'] * 3 + counter[']'] * 57 + counter['}']\
                         * 1197 + counter['>'] * 25137
    print('The answer to part 1 is: {}'.format(syntax_error_score))
    comp_scores = list()
    for item in incomplete:
        comp_scores.append(auto_comp_score(item))
    comp_scores = sorted(comp_scores)
    middle = (len(comp_scores) - 1) // 2
    print('The answer to part 2 is: {}'.format(comp_scores[middle]))