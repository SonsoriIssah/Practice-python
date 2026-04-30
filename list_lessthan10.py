def less_than_10(a:list)->list:
    new = [i for i in a if i<10]
    return new

print(less_than_10(  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
))