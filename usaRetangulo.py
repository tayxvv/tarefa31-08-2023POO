from Retangulo import Retangulo
from Ponto import Ponto

retangulo1 = Retangulo(10, 20, Ponto(1, 2))
retangulo3 = Retangulo(30, 20, Ponto(3, 1))

while True:
    print("1 - Encontrar centro")
    print("2 - Mudar tamanho")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saida1 = retangulo1.encontrar_centro()
        saida2 = retangulo3.encontrar_centro()
        print(saida1.x, saida1.y)
        print(saida2.x, saida2.y)
    elif opcao == "2":
        print("Digite a nova largura:")
        largura = int(input())
        print("Digite a nova altura:")
        altura = int(input())
        retangulo1.mudar_tamanho(largura, altura)
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")
        continue
    
    print("-----------------------------")