#ejercicio 1
'''1.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
resto. Escribir un programa que pregunte al usuario su nombre y sexo, y
muestre por pantalla el grupo que le corresponde.'''
nombre=input("Ingrese su nombre: ")
sexo=input("Ingrese su sexo: ")
new_nombre=nombre.lower()

if sexo=='femenino' and new_nombre[0]<'m' or sexo=='masculino' and new_nombre[0]>'n':
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")
 

#ejercicio 2

''''Para tributar un determinado impuesto se debe ser mayor de 16 años y
tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no.'''

edad=int(input("Ingrese su edad"))
ingresos=float(input("Ingrese sus ingresos mensuales"))

if edad > 16 and ingresos >= 1000:
    print(f"Si puedes tributar tu edad es de {edad} y tu ingreso es de {ingresos}")
else:
    print("No puedes tributar")

'''ejercicio 3
Escribir un programa para una empresa que tiene salas de juegos para
todas las edades y quiere calcular de forma automática el precio que debe
cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años
puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de
18 años, 10€.'''

edad=int(input("Ingrese su edad"))

if edad<4:
    print(f"Puedes entrar gratis tienes {edad} años")
elif edad >=4 and edad<18:
    print(f"Debes de pagar 5  tu edad esta entre 4 y 18 años{edad}")
else:
    print(f"Debes de pagar 10 tienes mas de 18 años {edad}")

'''ejercicio 4
4.- Escribir un programa que almacene la cadena de caracteres contraseña en
una variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable
sin tener en cuenta mayúsculas y minúsculas.'''

contraseña="aeamongol"
contranueva=input("Ingrese la contraseña").lower()

if contranueva == contraseña:
    print("contraseña correcta")
else:
    print("contraseña incorrectaaa")