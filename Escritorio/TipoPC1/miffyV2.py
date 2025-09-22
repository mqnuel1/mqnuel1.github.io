def frase():
    frases = input("Ingrese una frase(mínimo 50 caracteres): ")
    while len(frases) < 50 or frases.isalpha() == True:
        print("La frase es muy corta o contiene números, por favor ingrese correctamente la frase.")
        frases = input("Ingrese una frase(mínimo 50 caracteres): ")
    numero = len(frases) - frases.count(" ")
    print("Cantidad de caracteres(incluyendo espacios en blanco): ", len(frases))
    print("Cantidad de letras(sin espacios en blanco): ",numero)
    print("Frase de posición 20 al 40: ", frases[20:40])
    print("Frase en mayúsculas: ", frases.upper())
    print("Frases separada: ")
    for palabra in frases.split(" "):
        print(palabra)
def cuadrado(opc):
    for i in range((opc * 10)):
        print("Número Cuadrado Cubo")
        print(i+1, " ", (i+1) ** 2, " ", (i+1) ** 3)
def saltos(opc, peronaje):
    N = 10 * opc
    saltos = 0
    for i in range(1, N + 1):
        saltos = saltos + (5 - i) / (i + 1)
    print(f"La cantidad de saltos de {personaje} es de {saltos}")
while True:
    try:
        print("""
⠀⠀⢠⣾⠿⢿⣦⠀⠀⠀⠀⠀⠀⣤⣶⠶⣶⡄⠀
⠀⠀⢸⡇⠀⠀⠹⣧⠀⠀⠀⠀⣼⡟⠀⠀⢸⣿⠀
⠀⠀⢸⡇⠀⠀⠀⣿⡄⠀⠀⢠⣿⠀⠀⠀⢸⣿⠀
⠀⠀⠸⣷⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠀⣼⡟⠀
⠀⠀⠀⢿⡆⠀⠀⠘⠿⠿⠿⠿⠃⠀⠀⢰⣿⠀⠀
⠀⠀⣰⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠀⠀
⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀
⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧
⢸⣿⠀⠀⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⣿
⠸⣿⠀⠀⠀⠀⠀⠀⢶⣄⣤⠶⠀⠀⠀⠀⠀⠀⣿
⠀⠸⣧⡀⠀⠀⠀⠀⠺⠋⠙⠷⠀⠀⠀⠀⠀⣰⡃
⠀⠀⠘⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠟⠀
⠀⠀⠀⠀⠉⠛⠻⠷⠿⠿⠿⠿⠿⠿⠛⠛⠁⠀⠀""")
        print("Bienvenidos al mundo de Miffy y sus amigos")
        print("1. Miffy")
        print("2. Melany")
        print("3. Snuffy")
        print("4. Boris")
        print("5. Poppy")
        print("Creado por Dick Bruna en Países Bajos.")
        opc = int(input("Elija una opción: "))
        match opc:
            case 1:
                print("Has elegido a Miffy")
                personaje = "Miffy"
                break 
            case 2:
                print("Has elegido a Melany")
                personaje = "Melany"
                break
            case 3:
                print("Has elegido a Snuffy")
                personaje = "Snuffy"
                break
            case 4:
                print("Has elegido a Boris")
                personaje = "Boris"
                break
            case 5:
                print("Has elegido a Poppy")
                personaje = "Poppy"
                break
            case other:
                print("Opción no válida")
    except ValueError:
        print("No es una opción válida, inténtelo nuevamente")
frase()
saltos(opc, personaje)
cuadrado(opc)