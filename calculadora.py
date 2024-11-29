def calculadora():
    operacion = input("Ingresa la operación (suma, resta, multiplicacion, division): ").lower()
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == "suma":
        print(f"El resultado de la suma es: {num1 + num2}")
    elif operacion == "resta":
        print(f"El resultado de la resta es: {num1 - num2}")
    elif operacion == "multiplicacion":
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    elif operacion == "division":
        if num2 != 0:
            print(f"El resultado de la división es: {num1 / num2}")
        else:
            print("No se puede dividir por cero.")
    else:
        print("Operación no válida.")

calculadora()
