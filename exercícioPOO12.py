from abc import ABC, abstractmethod



class Lutador(ABC):

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_nivelpoder(self):
        pass

    @abstractmethod
    def atacar(self):
        pass



class Saiyajin(Lutador):
    def __init__(self, nome, nivelpoder):
        self.nome = nome
        self.nivelpoder = nivelpoder


    def get_nome(self):
        return self.nome
    
    
    def get_nivelpoder(self):
        return self.nivelpoder
    

    def atacar(self):
        return f"\n{self.nome} (Saiyajin) lançou um kamehameha com nível de poder de: {self.nivelpoder * 2}\n"
    



class Androide(Lutador):
    def __init__(self, nome, nivelpoder):
        self.nome = nome
        self.nivelpoder = nivelpoder


    def get_nome(self):
        return self.nome
    

    def get_nivelpoder(self):
        return self.nivelpoder
    

    def atacar(self):
        return f"\n{self.nome} (Androide) disparou um raio de energia infinito!\n"
    


class Namekuseijin(Lutador):
    def __init__(self, nome, nivelpoder):
        self.nome = nome
        self.nivelpoder = nivelpoder


    def get_nome(self):
        return self.nome
    

    def get_nivelpoder(self):
        return self.nivelpoder
    

    def atacar(self):
        return f"\n{self.nome} (Namekuseijin) esticou o braço e desferiu um golpe poderoso!\n"
    


def cadastrar_lutador():
    try:
        nome = input("\nDigite o nome do lutador: ").strip()
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        
        
        poder = int(input("Digite o nível de poder: "))
        if poder <= 0:
            raise ValueError("O nível de poder deve ser um número positivo!")
        

        print("\nEscolha a raça:")
        print("1- Saiyajin")
        print("2- Androide")
        print("3- Namekuseijin\n")

        opcao = input("Opção: ")


        if opcao == "1":
            lutador = Saiyajin(nome, poder)
        

        elif opcao == "2":
            lutador = Androide(nome, poder)
        

        elif opcao == "3":
            lutador = Namekuseijin(nome, poder)
        

        else:
            print("\nRaça inválida\n")
            return None
        
        return lutador
        
    except ValueError as e:
        print("Erro:", e)
        return None
    


def main():
    lutadores = []


    while True:
        print("\n====TORNEIO DE ARTES MARCIAIS====")
        print("1- Cadastrar lutador")
        print("2- Listar lutadores")
        print("3- Simular ataque")
        print("4- Sair")

        opcao = input("\nEscolha: ")


        if opcao == "1":
            lutador = cadastrar_lutador()
            if lutador:
                lutadores.append(lutador)
                print("\nLutador cadastrado com sucesso!\n")


        elif opcao == "2":
            if not lutadores:
                print("\nNenhum lutador inscrito\n")

            else:
                for i, l in enumerate(lutadores):
                    print(f"{i+1} - {l.get_nome()}({l.__class__.__name__}), Poder: {l.get_nivelpoder()}")


        elif opcao == "3":
            if not lutadores:
                print("\nNenhum lutador para lutar.\n")

            else:
                for l in lutadores:
                    print(l.atacar())


        elif opcao == "4":
            print("\nEncerrando o programa...até mais\n")
            break


        else:
            print("\nOpção inválida, tente novamente.\n")






if __name__ == "__main__":
    main()