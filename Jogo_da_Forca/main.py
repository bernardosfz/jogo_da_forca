import os
def limpartela():
    os.system ("cls")

limpartela()
jogar = True
while jogar == True:
    nomeDasafiante = input("Digite o nome do Dasafiante: ")
    nomeCompetidor = input("Digite o nome do Competidor: ")
    winner = ''
    loser = ''
    print("Nome do Desafiante:",nomeDasafiante)
    print("Nome do Desafiante:",nomeCompetidor)

    input("Enter para digitar a palavra chave...")
    limpartela()

    palavra = input("Digite a palavra chave: ").upper()

    dicas = []
    i = 1
    while i <= 3:
        for dica in range(0,3):
            dica = input("Digite a dica número " +str(i)+ ": ")
            dicas.append(dica)
            i += 1
    print("Palavra Chave e dicas registradas!")

    input("Enter para iniciar o jogo...")
    limpartela()

    inicial = """
    """
    cabeca = """
        O
    """
    tronco = """
        O
        |
    """
    braco_direito = """
        O
       /|
    """
    braco_esquerdo = """
        O
       /|\\
    """
    perna_direita = """
        O
       /|\\
       /
    """
    perna_esquerda = """
        O
       /|\\
       / \\
    """
    boneco = [
        inicial,
        cabeca, 
        tronco, 
        braco_direito, 
        braco_esquerdo,
        perna_direita, 
        perna_esquerda]

    j = 0
    acertos = 0
    erros = 0
    letrasCertas = ''
    letrasErradas = ''

    while acertos != len(palavra) and erros != 7:
        palavraEscondida = ''

        for letra in palavra:
            if letra in letrasCertas:
                palavraEscondida += letra + ' '
            else:
                palavraEscondida += '_ '

        print(boneco[erros])
        print(palavraEscondida)
        print("Você errou a letra: " + letrasErradas)

        escolha = int(input("Jogar (1) Pedir Dica (2): "))
        if escolha == 1:
            letra = input("Digite uma letra: ").upper()
        elif escolha == 2 and j == 3:
            print("Acabaram as dicas")
            letra = input("Digite uma letra: ").upper()
        elif escolha == 2:
            print("Jogador escolheu 'Pedir Dica'")
            print(dicas[j])
            letra = input("Digite uma letra: ").upper()
            j +=1
        else:
            print("Entrada Inválida")

        if letra in palavra:
            letrasCertas += letra
            acertos += palavra.count(letra)
        else:
            letrasErradas += letra + ' '
            erros += 1

    if erros == 6:
        winner = "Desafiante " + nomeDasafiante
        loser = "Competidor " + nomeCompetidor
    else:
        winner = "Competidor " + nomeCompetidor
        loser = "Desafiante " + nomeDasafiante

    print("Vencedor: ", winner)
    print("Perdedor: ", loser)

    input("Enter para ver o histórico...")
    limpartela()

    relatorio = open("historico_jogo_da_forca.txt","a")
    relatorio.write("Palavra: "+ palavra + " -" + " Vencedor: " + winner + " -" + " Perdedor: " + loser + "\n")
    relatorio.close()

    relatorio = open("historico_jogo_da_forca.txt","r")
    for i in relatorio:
        print(i)

    decider = int(input("Digite (1) para jogar novamente e (2) para sair: "))
    if decider == 1:
        jogar = True
    else:
        jogar = False
        break