def suma(n,ar):
    i = 0
    sum = 0    
    while  i<=n-1:
        sum+=ar[i]
        i+=1
    print sum
        


n=int(raw_input('elemento'))
ar=map(long,raw_input('ar').rstrip().split())
print ar
suma(n,ar)
