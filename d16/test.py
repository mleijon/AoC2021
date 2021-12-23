
def test(x):
    x += 1
    print(x)
    if x > 10:
        return
    else:
        return test(x)


x = 1
test(x)
print('end')
