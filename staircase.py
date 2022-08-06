def staircase(n):
    i = 1
    while i <= n:
        print i*'#'
        i+=1

n = int(raw_input('Cantidad'))

staircase(n)
