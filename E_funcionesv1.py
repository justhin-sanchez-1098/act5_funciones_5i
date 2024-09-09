print("manejo de funciones v1")
def hola_mundo():
    print("hola aqui estoy")
    
def Mensa(msg):
    print(msg)
def escribeNC(nombre,apellido):
    print(nombre, apellido)
    print(f"tu nombre completo es {nombre} {apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return f"la suma de {n1} y de {n2} es de:",s
    
# llamando a la funcion
hola_mundo()
Mensa("hola whatsAPP") # llama a mensa con 1 parametro
Mensa("el profe me sorprendio enviando wasaaa")# llama a mensa con 1 parametro
escribeNC("justhin", "medina")
print("funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))