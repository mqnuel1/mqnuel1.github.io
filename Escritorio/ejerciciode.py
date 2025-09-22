def dibujo():
    print(" - - -"*10)
    print("""
                    ⠀⠀⠀⢀⡴⠶⢶⡀⠀⠀⠀⣠⡴⢦⡀⠀⠀⠀
                    ⠀⠀⠀⡞⠀⠀⠀⢻⠀⠀⣰⠋⠀⠀⢹⡄⠀⠀
                    ⠀⠀⢸⡇⠀⠀⠀⠈⡇⠀⡟⠀⠀⠀⢸⠇⠀⠀
                    ⠀⠀⢸⡇⠀⠀⠀⠀⣇⢸⡇⠀⠀⠀⢸⠃⠀⠀
                    ⠀⠀⠘⡇⠀⠀⠀⠀⡇⢸⠀⠀⠀⠀⡞⠀⠀⠀
                    ⠀⠀⠀⣹⠀⠀⠀⠀⠛⠛⠀⠀⠀⠼⣅⠀⠀⠀
                    ⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀
                    ⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄
                    ⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇
                    ⣯⠀⠀⢰⡆⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠀⢸⠇
                    ⠹⣄⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀
                    ⠀⠙⠦⣤⣀⠀⠀⠛⠛⠂⠀⢀⣀⡤⠞⠃⠀⠀
                    ⠀⠀⠀⠀⠉⠉⠉⠛⠛⠉⠉⠉⠁          
            """)
    print(" - - -"*10)

def menu_principal():
    print("______"*10)
    print("\nBienvenido al mundo de la conejita Miffy y sus amigos!")
    print("Ingrese la opcion de su personaje favorito para el juego: ")
    print(" 1. Miffy")
    print(" 2. Melany")
    print(" 3. Snuffy")
    print(" 4. Boris")
    print(" 5. Poppy")
    print("Creado por Dick Bruna en Paises Bajos")
    print("______"*10)

dibujo()
menu_principal()
while True:
    try:
        opc = int(input("\nOpcion: "))
        if opc < 1 or opc > 5:
            print("\n - Opcion fuera de rango - ")
        else:
            print("Opcion ingresada correctamente!")
            break
    except ValueError:
        print("\n - No eligio una opcion valida! - ")
match opc:
    case 1:
        print("Usted eligio a MIFFY")
    case 2:
        print("Usted eligio a MELANY")
    case 3:
        print("Usted eligio a SNUFFY")
    case 4:
        print("Usted eligio a BORIS")
    case 5:
        print("Usted eligio a POPPY")
        