import random

historial = []
ganadas = 0
perdidas = 0
empates = 0

def mostrar_menu():
    print("\n=== Menu Principal ===")
    print("1. Jugar")
    print("2. Ver historial")
    print("3. Salir")

def mostrar_juego():
    print("\n=== Escoja que va a sacar ===")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Volver al menu principal")

while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opcion (1-3): "))
        if opcion == 1:
            while True:
                mostrar_juego()
                try:
                    eleccion = int(input("Ingrese su eleccion (1-4): "))
                    if eleccion == 4:
                        break
                    if eleccion < 1 or eleccion > 4:
                        print("Opcion fuera de rango")
                        continue
                except ValueError:
                    print("No ingreso una opcion valida")
                    continue

                opciones = ["Piedra", "Papel", "Tijera"]
                jugador = opciones[eleccion - 1]
                maquina_num = random.randint(1, 3)
                maquina = opciones[maquina_num - 1]
                print(f"Tu elegiste: {jugador}")
                print(f"La maquina eligio: {maquina}")

                if jugador == maquina:
                    resultado = "Empate"
                    empates += 1
                elif (jugador == "Piedra" and maquina == "Tijera") or (jugador == "Papel" and maquina == "Piedra") or (jugador == "Tijera" and maquina == "Papel"):
                    resultado = "Ganaste"
                    ganadas += 1
                else:
                    resultado = "Perdiste"
                    perdidas += 1

                historial.append(f"Tu: {jugador} | Bot: {maquina} | Resultado: {resultado}")
                print(f"Resultado: {resultado}")

        elif opcion == 2:
            print("\n=== Historial de partidas ===")
            if not historial:
                print("No ha jugando ninguna partida")
            else:
                for partida in historial:
                    print(partida)
                print("\nLos resultados son:")
                print(f"Ganaste: {ganadas} veces")
                print(f"Perdiste: {perdidas} veces")
                print(f"Empataste: {empates} veces")
        elif opcion == 3:
            print("Saliendo del programa")
            break
        else:
            print("Opcion fuera de rango")
    except ValueError:
        print("No ingreso una opcion valida")