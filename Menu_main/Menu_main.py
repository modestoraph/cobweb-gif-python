import funcoes
import cobweb

def menu_cobweb():

    print("Gere um cobweb")

################### Criação do Menu e Tratamento de Erro #######################

    while True:
        print("Escolha a função:")
        print("1 - Logística")
        print("2 - Reta")
        print("3 - Raiz")
        print("4 - Cosseno")
        print("5 - Expansora")

        try:
            opcao = int(input("Digite a opção: "))
            if opcao in [1, 2, 3, 4, 5]:
                break
            else:
                print("Erro! Escolha uma das opções válidas.")
        except ValueError:
            print("A opção deve ser um número inteiro.")

    while True:
        try:
            r = float(input("Digite o valor de r: "))
            break
        except ValueError:
            print("Erro! O valor de r deve ser um número do tipo float.")

    s = 0
    if opcao == 2:
        while True:
            try:
                s = float(input("Digite o valor de s: "))
                break
            except ValueError:
                print("Erro! O valor de s deve ser um número do tipo float.")

    while True:
        try:
            x0 = float(input("Digite o valor inicial x0: "))
            break
        except ValueError:
            print("Erro! O valor de x0 deve ser um número do tipo float.")

    while True:
        try:
            itera_max = int(input("Digite o número de iterações itera_max: "))
            if itera_max >= 1:
                break
            else:
                print("O número de iterações deve ser do tipo inteiro positivo.")
        except ValueError:
            print("Erro! O número de iterações deve ser um número inteiro.")

    F = Funcao(r, s)

    if opcao == 1:
        f = F.logistica
    elif opcao == 2:
        f = F.reta
    elif opcao == 3:
        f = F.raiz
    elif opcao == 4:
      f = F.cosseno
    elif opcao == 5:
       f = F.expansora
    else:
        print("Opção de função inválida.")
        return

    try:
        print("Gráfico dos valores dos iterados")
        val_iterados(f, x0, itera_max)
    except Exception as erro:
        print(f"Erro ao plotar o gráfico: {erro}")

    # Animação do Cobweb (Geração do GIF)
    try:
        cobweb(f, x0, itera_max, limite_x=(0, 1), filename='cobweb.gif')
    except Exception as erro:
        print(f"Erro ao gerar o GIF: {erro}")
