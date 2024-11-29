# Lista de estudiantes
estudiantes = ["Juan", "Ana", "Luis", "Carlos"]

# Diccionario de contacto
contacto = {
    "Juan": {"email": "juan@email.com", "ciudad": "Bogotá"},
    "Ana": {"email": "ana@email.com", "ciudad": "Medellín"},
    "Luis": {"email": "luis@email.com", "ciudad": "Cali"}
}

# Función para agregar un estudiante a la lista
def agregar_estudiante():
    nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado a la lista de estudiantes.")

# Función para actualizar la información de contacto en el diccionario
def actualizar_contacto():
    nombre = input("Ingresa el nombre del estudiante cuyo contacto deseas actualizar: ")
    if nombre in contacto:
        nuevo_email = input(f"Ingresa el nuevo correo de {nombre}: ")
        nueva_ciudad = input(f"Ingresa la nueva ciudad de {nombre}: ")
        contacto[nombre] = {"email": nuevo_email, "ciudad": nueva_ciudad}
        print(f"La información de contacto de {nombre} ha sido actualizada.")
    else:
        print(f"No se encuentra el estudiante {nombre} en el diccionario de contactos.")

# Menú para elegir la acción
print("Seleccione una opción:")
print("1. Agregar estudiante")
print("2. Actualizar contacto de estudiante")
opcion = input("Ingresa el número de la opción: ")

if opcion == "1":
    agregar_estudiante()
elif opcion == "2":
    actualizar_contacto()
else:
    print("Opción no válida.")
