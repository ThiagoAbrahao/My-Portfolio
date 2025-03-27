while True:
    começar = input("Digite 'começar' para iniciar o jogo").strip().lower()
    if começar == "começar":
        resposta = 77
        print("Vamos brincar de adivinhação, vou pensar em um número de 1 a 100 e você vai adivinha-lo.")
        while True:
            palpite = int(input("Qual seu palpite ?"))
            if palpite != 77:
                print("Você errou, tenta de novo")
            elif palpite == 77:
                print("Parabéns, você ganhou o jogo.")
                print("Obrigado por jogar :)")
                break



