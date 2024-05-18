num=int(input("Ingrese un número entero positivo: "))
contador=""
for i in range(num,0,-1):
    contador+=str(i)+","
print(contador[:-1])