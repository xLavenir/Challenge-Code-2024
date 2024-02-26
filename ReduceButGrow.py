def grow(arr):
    
    result = 1
    
    for i in arr:
        result = result*i
    return result

hasil = grow([1,2,3,4])
print(hasil)