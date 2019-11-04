a=int(input("digite el numero: "))
palabra = input("ingrese palabra: " )
i=0
alreves = ""
j= len(palabra)-1
while(i <= j):
    alreves = alreves + palabra[j]
    j=j-1

if(a==alreves):
    print("es Plindormo")