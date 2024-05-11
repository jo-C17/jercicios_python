'''
#primer ejercicio
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
redon1=round(num1)
redon2=round(num2)
print(f"Suma de {redon1}+{redon2}= {redon1+redon2}")
print(f"Resta de {redon1}-{redon2}= {redon1-redon2}")
print(f"Multiplicacion  de {redon1}x{redon2}={redon1*redon2}")
print(f"Division de {redon1}/{redon2}={redon1/redon2}")
print(f"Division entera de {redon1}//{redon2}={redon1//redon2}")
print(f"Residuo de {redon1}%{redon2}={redon1%redon2}")

#Segundo Ejercicio
num_entero=int(input("Ingrese un número entero: "))
print(f"El cuadrado de {num_entero} es = {num_entero**2}")
print(f"El cubo de {num_entero} es = {num_entero**3}")

#Tercer Ejercicio
num_ente=int(input("Ingrese un número entero: "))

if num_ente == 0:
    print("El valor es cero")
elif num_ente > 0:
    print("El valor es positivo")
else:
    print("El valor es negativo")
#cuarto ejercicio
divi=int(input("Ingrese un número entero: "))

if divi%3==0 and divi%5==0:
    print("El numero es divisible entre 3 y 5")
else:
    print("No es divisible entre 3 y 5")    

#5to ejercicio

calificacion=10

if calificacion >=90 and calificacion<100:
    print("Calificacion |A|")
elif calificacion >=80 and calificacion<89:
    print("Calificacion |B|")
elif calificacion>=70 and calificacion<79:
    print("Calificacion |C|")
elif calificacion>=60 and calificacion<69:
    print("Calificacion |D|")
elif calificacion<60:
    print("Calificacion |F|")
elif calificacion>100:
    print("La calificaicon no puede ser mayor de 100")
else:
    print("ERROR")'''
#Sexto ejercicio

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))

if a>b and a>c:
    print(f"El mayor es {a}")
elif b>a and b>c:
    print(f"El mayor es {b}")
else:
    print(f"El mayor es {c}")
'''
#Septimo ejercicio
entero=int(input("Ingrese un número entero: "))
if entero%2==0:
    print("El numero es par")
else:
    print("El numero es impar")
'''