def _plusMinus(arr):
    pos = 0
    neg = 0
    zeros = 0
    arr_i = 0
    while arr_i < len(arr):
        if arr[arr_i] < 0:
            neg +=1
        elif arr[arr_i] > 0:
            pos+=1
        else:
            zeros+=1
        arr_i+=1

    return round(pos/float(len(arr)),5), round(neg/float(len(arr)), 5), round(zeros/float(len(arr)),5)
    
   
    
    




n = int(raw_input('Cantidad de Elementos'))
arr = map(int, raw_input('Elementos').rstrip().split())

print _plusMinus(arr)
