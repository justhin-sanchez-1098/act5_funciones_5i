print("funciones creadas por el usuario")

def mi_lista():
    amigos=["pao", "emi", "wicho"]
    for justhin in amigos:
        print(justhin)
# llamadas a funciones
mi_lista()

#tuplas
print("")
print("--tuplas--")
arcoiris = ("rojo", "verde", "azul")
for elcolor in arcoiris:
    print(elcolor)
    
    #conjuntos
print("")
print("--conjuntos--")
amigos = {"pao","wicho", "emi"}
for i in amigos:
    print(i)
    
#diccionarios
print("")
print("--diccionarios--")
carros = {
    "honda": "civic",
    "ford": "focus",
    "chevrolet": "camaro", 
}
for x in carros:
    print(carros[x])    

