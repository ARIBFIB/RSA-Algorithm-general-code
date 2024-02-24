def mod_function(base, pow, n):
    p = base % n
    to_binary = str(bin(pow))
    array=[char for char in to_binary]
    x=1
    for xx in range(len(array)-1,-1,-1):
        if array[xx]=='1':
            x=(x*p) % n
        p=(p*p) % n
    return x
print(mod_function(9,756,31))
