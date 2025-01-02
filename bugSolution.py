def function(x):
    fib_numbers = [0, 1]
    if x <= 1:
        return fib_numbers[x]
    else:
        for i in range(2, x + 1):
            next_fib = fib_numbers[i - 1] + fib_numbers[i - 2]
            fib_numbers.append(next_fib)
        return fib_numbers[x]