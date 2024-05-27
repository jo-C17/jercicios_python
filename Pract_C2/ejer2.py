'''Escribir un programa que pregunte al usuario una cantidad a invertir, el
interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión.'

cantidad_invertir=float(input("Ingrese la cantidad a invertir: "))
interes_anual=float(input("Ingrese el interes anual: "))
numero_anios=int(input("Ingrese el número de años: "))
porcent=interes_anual/100
for años in range(1,numero_anios+1):
    monto_final=cantidad_invertir*(1+porcent)**años
    print(f"Año {años}:{monto_final:.1f}")'''


'''Escribir un programa que muestre por pantalla la tabla de multiplicar del
1 al 10.'''
num=int(input("Ingrese la tabla a multiplicar: "))
for i in range(1,11):

    print(f"{i}X{num}={i*num}")

  