# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Condicional para verificar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usar un bucle for para imprimir los cuadrados de los números
for n in numeros:
    print(f"El cuadrado de {n} es {n**2}")

# Usar un bucle while para solicitar un número hasta que sea mayor que 10
while numero <= 10:
    numero = int(input("Ingresa un número mayor que 10: "))
print(f"El número ingresado es {numero}")
