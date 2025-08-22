def is_permutation(n, m):
    n = str(n)
    m = str(m)
    for c in n:
        if n.count(c) != m.count(c):
            return False
    return True

for number in range(1, 10**6 + 1):
    for mult in range(2, 7):
        if not is_permutation(number, number * mult):
            break
    else:
        print(number)
        break
