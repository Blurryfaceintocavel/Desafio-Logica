# Desafio DIO 

# Desafio DIO 

while True:

    Heroi = input("Digite o nome do héroi: ")
    XP = int(input("Digite a quantidade de XP: "))

    # Classificação corrigida
    if XP < 1000:
        faixa = "Ferro"
        
    elif 1001 <= XP <= 2000:
        faixa = "Bronze"
        
    elif 2001 <= XP <= 5000:
        faixa = "Prata"
        
    elif 5001 <= XP <= 7000:
        faixa = "Ouro"
        
    elif 7001 <= XP <= 8000:
        faixa = "Platina"
        
    elif 8001 <= XP <= 9000:
        faixa = "Ascendente"
        
    elif 9001 <= XP <= 10000:
        faixa = "Imortal"
        
    else:
        faixa = "Radiante"

    # Efeito visual
    for i in range(3):
        print("Carregando Informações...")

    print(f"\n[Carregamento completo]\nO herói de nome {Heroi} está no nível {faixa} com {XP} pontos de XP")

    repetir = input("Deseja classificar outro herói? (s/n) ").lower()
    if repetir != "s":
        break
