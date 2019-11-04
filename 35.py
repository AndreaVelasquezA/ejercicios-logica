def maymen(a,b,c):
    if(a>b and a>c):
        print("es mayor",a)
    elif(b>a and b>c):
        print("es mayor",b)
    elif(c>a and c>b):
        print("es mayor",c)
    if(a<b and a<c):
        print("es menor",a)
    elif(b<a and b<c):
        print("es menor",b)
    elif(c<a and c<b):
        print("es menor",c)
    
maymen(1,4,6)