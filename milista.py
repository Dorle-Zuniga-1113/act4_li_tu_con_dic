#ejemplo de uso de listas
misnovias = ["Mariana", "Melanie cineeeee!", "Daniela"]
misNumeros=[666,77,10]
# mostrando mis novias 
print(misnovias)
# mostrando mis numeros raros
print(misNumeros)
print ("---accediendo a la lista---")
print(misnovias[-2])
if "Maria" in misnovias :
    print ("si, 'Maria' está en la lista de mis novias")
else:
    print("chale, no eres mi novia")
    print("Numero de novias")
Nnovias=len(misnovias)
print(f"Numeros de novias = {Nnovias}")
print("chale, no eres mi novia")
print("ciclo for en listas")
posicion=0
for medianaranja in misnovias:
    print(medianaranja,"",posicion)
    posicion=posicion+1