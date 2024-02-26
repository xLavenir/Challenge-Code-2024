def reverse_seq(n):
    
    arr = []
    
    while n >=1:
        arr.append(n)
        n-=1
    return arr

hasil = reverse_seq(5)
print(hasil)