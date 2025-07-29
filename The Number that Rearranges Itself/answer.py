# function returns a sorted list if sorted(str(x)) == sorted(str(y))
def is_it_a_permutation(x, y):
    return sorted(str(x)) == sorted(str(y))

# This brute forces the solution by checking all numbers from 1 to 100 million using the above function
def test_function():
    for p in range(1,100000000):
        result = []
        for i in range(2,7):
            result.append(is_it_a_permutation(p,p*i))
        if all(result):
            return p

print(test_function())