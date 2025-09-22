class Personagem:
    def __init__(self, nome, nivel):
        self._nome = nome
        self._nivel = nivel


    
    def atacar(self):
        print(f"\n{self._nome}, realizou um ataque!")



class Guerreiro(Personagem):
    def __init__(self, nome, nivel, força):
        super().__init__(nome, nivel)
        self.força = força


    def atacar(self):
        print(f"\n{self._nome} realizou um ataque de {self.força} de força!")



class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.mana = mana


    def atacar(self):
        print(f"\n{self._nome} realizou um ataque com {self.mana} de mana!\n\n")




def main():
    perso1 = Personagem("Arthur", 2)
    perso2 = Guerreiro("Jokes", 5, 50)
    perso3 = Mago("Flyn", 3, 80)


    lista_personagens = [perso1, perso2, perso3]

    for p in lista_personagens:
        p.atacar()








if __name__ == "__main__":
    main()