#ejemplo de manejo de lista
misnovias = ["lidia","maria","monse"]
misNumneros=[666, 77, 10]
# mostrando mis novias
print(misnovias)
# mostrando mis numeros raros
print(misNumneros)
print("--accedieno a los datos de las listas--")
print(misnovias[-2])
if "lidia" in misnovias:
    print("si, 'lidia' esta en la lista de mis novias")
else:
    print("chale no era mi novia")
print("Numero de novias")
Nnovias=len(misnovias)
print(f"Numero de novias = {Nnovias}")
print("ciclo for en listas")
posicion=0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1