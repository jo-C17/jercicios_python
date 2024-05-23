'''Escribir un programa que pida al usuario un número entero positivo
mayor que 2 y muestre por pantalla si es un número primo o no'''

num=int(input("Ingrese un número mayor que 2: "))
if num>2:
    for i in range(3,num+1):
        if num%i==0:
          print(f"{i} No es primo")
        else:
          print(f"{i} Es primo ")
else:
   print("El número tiene que ser mayor que 2")