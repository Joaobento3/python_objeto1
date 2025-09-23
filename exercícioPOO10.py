class Personagem:
    def __init__(self, nome, constelacao):
        self._nome = nome
        self._constelacao = constelacao



    def apresentar(self, nome, constelacao):
        print(f"\nEste é o {self._nome} um guerreiro muito forte que tem poderes da constelação de {self._constelacao}.\n")



class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.poder_de_luta = poder_de_luta


    def golpe_especial(self):
        print(f"\nO {self._nome} usa seu poder de {self.poder_de_luta}!\n")



class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_do_zodiaco):
        super().__init__(nome, constelacao)
        self.casa_do_zodiaco = casa_do_zodiaco


    def defender_casa(self):
        print(f"\nO {self._nome} usa sua defesa {self.casa_do_zodiaco} para defender a casa!\n")



class CavaleiroHíbrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        CavaleiroDeBronze.__init__(self, nome, constelacao, poder_de_luta)
        CavaleiroDeOuro.__init__(self, nome, constelacao, casa_do_zodiaco)



    

def main():

    cavaleiro_de_bronze = []
    cavaleiro_de_ouro = []
    cavaleiro_hibrido = []
    
    while True:
        print("\n=====-CAVALEIROS DO ZODÍACO: O último golpe-=====\n")
        print("Menu:")
        print("A. Cadastrar personagem")
        print("B. Listar todos personagens")
        print("C. Executar golpes especiais ou defesas")
        print("D. Sair do jogo")

        opcao = input("\nDigite o que deseja fazer (A-D): ")


        if opcao:
            if opcao == "A":
                nome_perso = input("\nNome: ")
                constelacao_perso = input("Constelação: ")
                cavaleiro_tipo = input("Qual cavaleiro voce deseja criar: (B)ronze, (O)uro ou (H)íbrido: ").strip().upper()
                    

                if nome_perso and constelacao_perso and cavaleiro_tipo:
                    if cavaleiro_tipo == "B":
                        personagem = CavaleiroDeBronze(nome, constelacao)
                        cavaleiro_de_bronze.append(personagem)
                        print("\nPersonagem cadastrado com sucesso!\n")

                    elif cavaleiro_tipo == "O":
                        cavaleiro_de_ouro.append(nome_perso, constelacao_perso)
                        print("\nPersonagem cadastrado com sucesso!\n")

                    elif cavaleiro_tipo == "H":
                        cavaleiro_hibrido.append(nome_perso, constelacao_perso)
                        print("\nPersonagem cadastrado com sucesso!\n")

                    else:
                        print("\nResposta inválida.\n")

                else:
                    print("\nNenhum dos campos pode estar vazio.\n")

            
            elif opcao == "B":

                if cavaleiro_de_bronze:
                    for p in cavaleiro_de_bronze:
                        p.apresentar()

                else:
                    print("\nNenhum cavaleiro de bronze foi encontrado.\n")

                if cavaleiro_de_ouro:
                    for p in cavaleiro_de_ouro:
                        p.apresentar()

                else:
                    print("\nNenhum cavaleiro de ouro foi encontrado.\n")
                    
                if cavaleiro_hibrido:
                    for p in cavaleiro_hibrido:
                        p.apresentar()

                else:
                    print("\nNenhum cavaleiro híbrido foi encontrado.\n")


            elif opcao == "C":
                
                if cavaleiro_de_bronze:
                    for p in cavaleiro_de_bronze:
                        p.golpe_especial()

                else:
                    print("\nNenhum cavaleiro de bronze foi encontrado.\n")

                if cavaleiro_de_ouro:
                    for p in cavaleiro_de_ouro:
                        p.casa_do_zodiaco()

                else:
                    print("\nNenhum cavaleiro de ouro foi encontrado.\n")
                    
                if cavaleiro_hibrido:
                    for p in cavaleiro_hibrido:
                        p.golpe_especial()
                        p.casa_do_zodiaco()

                else:
                    print("\nNenhum cavaleiro híbrido foi encontrado.\n")


            elif opcao == "D":
                print("\nSaindo do jogo...\n")
                break


            else:
                print("\nResposta inválida.\n")





if __name__ == "__main__":
    main()