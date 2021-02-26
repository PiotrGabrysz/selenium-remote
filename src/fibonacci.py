def get_n_fibonacci(n):
    a_1, a_2 = 0, 1

    if n > 2:
        for i in range(n - 2):
            a_1, a_2 = a_2, a_1 + a_2
        return a_2
    elif n == 2:
        return a_2
    elif n == 1:
        return a_1
    else:
        return False
