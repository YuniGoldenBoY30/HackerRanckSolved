# Dado una lista de numeros, devolver los impares apartir de un valor inicial
def even(start, n):
    # write your code here
    num = []
    while True:
        if start % 2 == 0:
            num.append(start)
        if len(num) == n:
            break
        start += 1
    return num


print(even(2, 4))