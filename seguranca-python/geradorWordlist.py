import itertools

resultado = itertools.permutations('abcdf', 5) 

for i in resultado:
    print(''.join(i))