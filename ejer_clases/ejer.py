'''frase=input("ingrese una frase: ")
letra =input("Ingrese una letra")

contador=0

for i in frase:
    if i==letra:
        contador+=1
print(contador)'''
asignatiras=["Matematica","fisica","quimica","comunicacion"]

notas=[]

for i in asignatiras:
    nota=input("Cual es tu nota: ")
    notas.append(nota)
print(notas)
for i in range(len(asignatiras)):
    print(f"en {asignatiras[i]} sacaste {notas[i]}")