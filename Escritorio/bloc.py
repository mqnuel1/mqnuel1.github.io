def prom(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

def resultado(promedio):
    if promedio < 11:
        print("Estado: Desaprobado")
    elif promedio >= 11 and promedio <= 16:
        print("Estado: Aprobado")
    else:
        print("Estado: Excelente")

while True:
    nombre = input("Ingrese nombre del estudiante (ingrese 'fin' para terminar): ")
    if nombre == "fin":
        break
    i = 1
    while i <= 3:
        try:
            nota = float(input(f"Nota {i}: "))
            if 0 <= nota <= 20:
                if i == 1:
                    n1 = nota
                elif i == 2:
                    n2 = nota
                else:
                    n3 = nota
                i += 1
            else:
                print("La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Error: ingrese un número válido.")
            
    p = prom(n1, n2, n3)
    print("\nResultados:")
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {p:.2f}")
    resultado(p)
    print("\n")
