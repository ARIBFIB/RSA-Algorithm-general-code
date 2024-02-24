def mod_func(base,pow, n):
    p = base % n
    to_bin = str(bin(pow))
    arr = [char for char in to_bin]
    x = 1
    for xx in range(len(arr)-1,-1,-1):
        if arr[xx] == '1':
            x = (x*p) % n
        p = (p*p) % n
    return x
print(mod_func(11,22,33))