def mensaje_fav_user():
    while True:
        mensaje = input("Ingrese un mensaje para su personaje de favorito:")
        if(len(mensaje)<50):
            print("Mensaje corto minimo de 50 letras")
        else:
            mensaje1 = mensaje.replace(" ","")
            print(f"Cantidad de caracteres(sin espacios en blanco):{len(mensaje1)}")
            print(f"Mensaje [20:40]:{mensaje[20:40]}")
            print(f"Mensaje en mayusculas:{mensaje.upper()}")
            for texto in mensaje.split(" "):
                if (texto == ""):
                    continue
                else:
                    print(f" {texto}")
            break

def dibujar():
    print(""" ⠀        ⣀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠉⠉⠻⣦⡀⠀⠀⠀⠀⠀⣴⠞⠛⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠈⣷⠀⠀⠀⢀⡾⠃⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡇⠀⠹⢦⡤⢤⣄⡀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⣾⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡴⠞⠋⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⢸⡇⠀⠀⠀⠀⠀⠀⠘⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢧⣄⡀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⠇⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣿⠀⠀⢀⣀⣀⣀⣱⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣤⠶⠋⠀⠈⠉⠁⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠘⠳⠛⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠸⠃⠐⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠐⠀⠀⠂⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠂⠀⢀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠀⠀⠀⠀⠊⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡟⠋⠙⣧⠀⠀⣰⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠛⠻⡧⠀⠀⢻⣄⡀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠁⠀⠀⠘⠛⠳⢦⣀⠀⠀⠀⢀⡀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⣤⣤⣤⡄⠀⢹⡆⠀⠀⠀⣽⡷⣿⡋⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡁⠸⣇⡀⣀⡤⠀⢸⡇⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢀⣠⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⠈⠛⠉⠀⣠⠞⠛⢳⡶⢤⣤⣤⣴⡶⠶⠶⠚⠛⢩⡿⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⢻⡁⠀⠀⠀⠙⠳⠶⠖⠛⠀⠀⠀⠀⣴⣋⣠⡾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣰⣾⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣌⠙⠳⢶⡶⠶⠶⠞⣫⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡞⢻⠄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠒⠛⠛⠶⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠉⠉⠀⠈⠳⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠂⠀⠀⠀⣤⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠷⠤⠶⢤⣀⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀""")

def func_cal_salto(N,personaje):
    N = N*10
    suma = 0
    i = 1
    while i <= N:
        suma += (5-i)/(i**2+1)
        i+=1
    print(f"La cantidad de saltos de {personaje} es de {suma:.2f}")

def mostrar_num():
    print(f"Número{' '*3}Cuadrado{' '*4}Cubo")
    for x in range(1, 10*user_input+1):
        print(f'{x:3d}{" "*7}{x**2:4d}{" "*6}{x**3:5,d}')
        
while True:
    try:
        print("---"*15)
        print(f"{"Bienvenido al mundo de Miffy":^20}")
        dibujar()
        print("1. Miffy")
        print("2. Melany")
        print("3. Snuffy")
        print("4. Boris")
        print("5. Poppy")
        print("Creado por Dick Bruna en Paises Bajos")
        user_input = int(input("Ingrese la opcion de su personaje favorito: "))
        if(1<= user_input <=5):
            break
    except ValueError:
        print("Error")
print("Personaje seleccionado correctamente")
match user_input:
    case 1:
        print("Su personaje favorito es Miffy")
        perso_fav = "Miffy"
    case 2:
        print("Su personaje favorito es Melany")
        perso_fav = "Melany"
    case 3:
        print("Su personaje favorito es Snuffy")
        perso_fav = "Snuffy"
    case 4:
        print("Su personaje favorito es Boris")
        perso_fav = "Boris"
    case 5:
        print("Su personaje favorito es Poppy")
        perso_fav = "Poppy"


func_cal_salto(user_input,perso_fav)

mensaje_fav_user()

mostrar_num()