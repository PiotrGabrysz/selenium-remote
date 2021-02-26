i = 0

if i > 0:
    print("Positive value")
elif i < 0:
    print("Negative value")
else:
    print("Null")


a, b = 0, 0

if a > 0 and b > 0:  # and, or, not
    print("values are positive")


if a is not 0:  # a != 0
    print("a is not null")
elif a is 0:  # a == 0
    print("a is null")
