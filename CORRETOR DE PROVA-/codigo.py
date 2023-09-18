gab = []
rep = []
nota = 0


def imprimirMenu():
    print("1 - Adicionar gabarito: ")
    print("2 - Adicionar Respostas: ")
    print("3 - Mostrar nota: ")
    print("4 - Mostrar quetões acertadas: ")
    print("5 - Mostrar quetões erradas: ")
    print("6 - Apagar respostas: ")
    print("0 - Sair: ")
    print("\n")


imprimirMenu()
aux = int(input())

while aux != 0:
    if aux == 1:
        quant = int(input("quantas questões deseja inserir? "))
        for i in range(quant):
            print(i+1," - Questão: ")
            gab.append(input())
        print("\n")    
    elif aux == 2:
        for i in range(len(gab)):
            print(i+1,"- Questão: ")
            rep.append(input())
        print("\n")
    elif aux == 3:
        nota = 0
        for i in range(len(rep)):
            if gab[i] == rep[i]:
                nota +=1
        print("Sua pontuação foi: ",nota,"\n")
    elif aux == 4:
        print("Certas: ")
        for i in range(len(rep)):
            if gab[i] == rep[i]:
                print(i+1)
        print("\n")
    elif aux == 5:
        print("Erradas: ")
        for i in range(len(rep)):
            if gab[i] != rep[i]:
                print(i+1)
        print("\n")
    elif aux == 6:
        rep.clear()
    

    

    imprimirMenu()
    aux = int(input())

print("Fim!")



    


