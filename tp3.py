# -*- coding: UTF-8 -*-

a = []

with open("test02.txt") as f:
    n = f.readline()
    n = int(n)
    a = []
    for u in f.readline().split():
        a.append(int(u))

    m = f.readline()
    m = int(m)

    with open("output.txt", "w") as f2:

        for i in range(m):
            i1, i2 = f.readline().split()
            i1 = int(i1)
            i2 = int(i2)
        
            j = i1
            s = 0 
            while j <= i2:
                s += a[j-1]
                j+=1
            
            f2.write('%d ' % s)
