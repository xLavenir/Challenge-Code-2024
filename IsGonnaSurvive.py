def hero(bullets, dragons):
    if bullets / 2 >= dragons:
        return True
    else:
        return False
    
test = hero(2,3)
print(test)