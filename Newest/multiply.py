def multiply(a, b, bound):
    write your code here
if a * b <= bound:
    return print(a * b)
raise ValueError(f"multiplication of {a} and {b} with bound {bound} not possible")


return print(a * b) if a * b <= bound else print()


multiply(2, 0, 10)
multiply(2, 5, 12)
multiply(2, 5, 9)