expression = input().strip().split()

def perform_operation(exp_or_smth_idk, operators):
    i = 0
    while i < len(exp_or_smth_idk):
        if exp_or_smth_idk[i] in operators:
            a = int(exp_or_smth_idk[i - 1])
            b = int(exp_or_smth_idk[i + 1])
            if exp_or_smth_idk[i] == '+':
                result = a + b
            elif exp_or_smth_idk[i] == '-':
                result = a - b
            elif exp_or_smth_idk[i] == '*':
                result = a * b
            elif exp_or_smth_idk[i] == '/':
                result = a // b
            exp_or_smth_idk = exp_or_smth_idk[:i - 1] + [str(result)] + exp_or_smth_idk[i + 2:] # mf took sooooo long to figure out!!!
            i = 0
        else:
            i += 1
    return exp_or_smth_idk

for op in ['+', '-', '*', '/']:
    expression = perform_operation(expression, [op])

print(expression[0])
