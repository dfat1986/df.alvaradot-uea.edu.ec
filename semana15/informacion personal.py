#Crear el diccionario inicial
informacion_personal = {
    "nombre": "Fernanda Gómez",
    "edad": 38,
    "ciudad": "Quito",
    "profesion": "Paramédico"
}

#Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

#Actualizar la clave de la profesión
informacion_personal["profesion"] = "Paramédico"

#Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "999-78654"

#Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir cada clave y valor usando iteración
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")