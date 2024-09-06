arcoirirs = ("azul", "rojo", "amarillo", "verde")
print(arcoirirs)
print("-longitud arcoiris--")
print(len(arcoirirs))
animales=("pantera","la pantera",20,"estatura",1,7)
print(animales)
print(animales[2])
rateros = ("john", "cisi", "lulu99")
y = list(rateros)
y[0] = "polainas"
x = tuple(y)

print(x)
print("agregando elementos")
Nanimal=("body","cheetos")
y=list(Nanimal)
print(y)
y.append("tontolin")
otratupla=tuple(y)
print(otratupla)
print("uso de for en tuplas")
for elcolor in arcoirirs:
    print(elcolor)
    