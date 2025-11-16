import random


heroi= input ("Digite o nome do herói: ")
contador= 0 
XP= random.randint (0, 12000)
    
if XP < 1000:
    faixa = "Ferro"
    
elif XP <=1001 and XP <= 2000:
    faixa = "Bronze"
    
elif XP <=2001  and XP <=5000:
    faixa = "Prata"
     
elif XP <=5001 and XP <=7000:
    faixa = "Ouro" 
  
elif XP <=7001 and XP <=8000:
    faixa = "Platina"
    
elif XP <=8001 and XP <=9000:
        faixa = "Ascendente"
        
elif XP >9001 and XP <=10000:
        faixa = "Imortal"   
else:
    faixa = "Radiante"
    
for i in range(3):
    print(f"Carregando Informações...")  
print (f" [Carregamento completo] \n O herói de nome {heroi} esta no nivel {faixa} com {XP} pontos de XP")
