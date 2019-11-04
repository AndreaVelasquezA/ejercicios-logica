def Rotacion(t):
    l = len(t)
    k = 1
    p1 = t[0]
    p2 = ""
    for k in range(1, l):
        if t[k].islower():
            p1 = p1 + t[k]
            k = k + 1
        else:
            p2 = p2 + t[k]
            k = k + 1
    print(p2 + p1)
 
 



Rotacion(andrea)
