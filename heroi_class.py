
class Heroi:
    def __init__(self, tipo):
        self.nome = None
        self.idade = None
        self.tipo = tipo
    
    def dado_hero(self):
        self.nome = input("Digite o nome do heroi: ")
        self.idade = input("Digite o idade do heroi: ")
        self.tipo = input("Digite o tipo (mago, guerreiro, monge, ninja): ")
    
    def atacar(self):
        if self.tipo == "mago":
            arma = "magia"
        elif self.tipo == "guerreiro":
            arma = "espada"
        elif self.tipo == "monge":
            arma = "artes marciais"
        elif self.tipo == "ninja":
            arma = "shuriken"
        else:
            print("Escolha uma classe valida")
            return
        print(f"O {self.nome} ataca com {arma}")


heroi = Heroi(None)
heroi.dado_hero()
heroi.atacar()
        
        