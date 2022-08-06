# # Write your code here
def minX(arr):
    # Write your code here
    c = 0
    s = 0
    while True:
        arr.insert(0, c)
        for i in arr:
            s += i
        if s >= 1:
            break
        c += 1
    return print(c)


#
#
minX([-5,4,-2,3,1])