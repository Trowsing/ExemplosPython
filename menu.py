# This code will count the people on a queue accoridng to its status 
# and print the number and type of attention whether it is for a disabled
# or a normal person, admin and user are both accessible from the main menu
# and they can choose from the options in a submenu.

senhaN = 100
senhaP = 0
turnos = []

def restart():
    senhaP = 0
    senhaN = 0
    print("Contagem reiniciada: N = ", senhaN,"P = ", senhaP)

def incorreto():
    print("Entrada invalida")
    menu()

def menu():
    global senhaP
    global senhaN
    print("Bem vindo, escolha uma opcao \n 1.- Admin \n 2.- Usuario")
    opcao = input()
    if opcao == 1:
        print("Admin, escolha uma opcao: \n 1.- Reiniciar contagem \n 2.- Proximo")
        opAdmin = input()
        if opAdmin == 1:
            restart()
            menu()
        if opAdmin == 2:
            if senhaP > 0:
                print("Chamando preferencial: ", turnos[0])
                turnos.pop(0)
                menu()
            else:
                print("Chamada normal: ", turnos[0])
                turnos.pop(0)
                menu()
        else:
            incorreto()
    if opcao == 2:
        print("Usuario, escolha uma opcao: \n 1.- Senha normal \n 2.- Senha preferencial")
        opUsuario = input()
        if opUsuario == 1:
            senhaN += 1
            turnos.append(senhaN)
            print("N", senhaN)
            print(turnos)
            menu()
        if opUsuario == 2:
            if senhaP == 99:
                senhaP = 0
            senhaP += 1
            turnos.append(senhaP)
            turnos.sort()
            print("P", senhaP)
            print(turnos)
            menu()
    else:
        incorreto()

menu()
