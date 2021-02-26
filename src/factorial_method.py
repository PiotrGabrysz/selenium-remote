def factorial(n):
    if n > 0:
        result = 1
        for i in range(1, n + 1):
            result *= i   # result = result * i
        return result
    elif n == 0:
        return 1
    else:
        return False


result = factorial(4)
print(result)
