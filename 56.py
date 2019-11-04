def sumpro(a):
    l=0
    p=0
    for i in range(1,a+1):
        if(i%2==0):
            p=p+i
        else:
            l=l+1
        
    prom1=p/a
    prom=l/a

  
    print("suma pares: ",p,"suma impares: ",l,"promedio pares:  ",prom1,"promedio impares",prom)

sumpro(5)
