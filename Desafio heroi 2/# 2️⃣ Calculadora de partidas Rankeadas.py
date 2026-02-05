# 2️⃣ Calculadora de partidas Rankeadas

'''
Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)
'''

def rankeada (vitoria, derrotas):
   rank = vitoria - derrotas 
   
   if rank < 10:
     titulo = "Ferro"
   elif  rank >=10 and rank <=20:
      titulo = "Bronze"
   elif 21 <= rank <=50:
      titulo = "Prata"
   elif 51 <= rank <=80:
      titulo = "Ouro"
   elif 81<= rank <=90:
      titulo = "Diamante"
   elif 91<= rank <=100:
      titulo = "Lendario"
   else:
      titulo = "Imortal"
      
   return rank, titulo
   
#dados usuarios 

vitoria = int(input("Digite a quantidade de vitórias: "))
derrotas= int(input("Digite a quantidade de derrotas: "))
   
rank, titulo = rankeada(vitoria, derrotas)
print(f"O herói tem saldo de {rank} e está no nível {titulo}")