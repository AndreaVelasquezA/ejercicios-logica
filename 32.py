def notas(n1,n2,n3,n4,n5):
    n1f=n1*0.15
    n2f=n2*0.20
    n3f=n3*0.15
    n4f=n4*0.30
    n5f=n5*0.20
    nf=(n1f+n2f+n3f+n4f+n5f)
    if(nf<2):
        print("no puede habilitar")
    elif(nf<3):
        print("reprobo")
    elif(nf>=3):
        print("aprobo")
    elif(nf>4,5):
        print("aprobo felicitaciones")

notas(3,5,4,2,3)

