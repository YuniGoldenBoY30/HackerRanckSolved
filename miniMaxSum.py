def miniMaxSum(arr):
    arr.sort()
    i = 1
    sum_arr = 0
    while i < len(arr)-1:
        sum_arr += arr[i]
        i+=1
    sum_outLast = arr[0] + sum_arr
    sum_outFirst = arr[-1] + sum_arr
    return sum_outLast, sum_outFirst 


arr = map(int, raw_input('Numeros').rstrip().split(' '))
print miniMaxSum(arr)
