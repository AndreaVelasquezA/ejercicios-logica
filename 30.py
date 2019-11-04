def iva(venta):
    print("valor original",venta)
    if(venta==150000):
        b=venta*0.05
        c=venta-b
    print("vlor con descuento: ",c)
    iva = c*0.19
    print("valor de iva",iva)
    viva = c+iva
    print("valor de venta con iva incluido",viva)
    
iva(150000)