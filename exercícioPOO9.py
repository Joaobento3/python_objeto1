class Participante:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

        def get_nome(self):
            return self._nome
        

        def get_email(self):
            return self._email
        

        def set_nome(self, nome):
            self._nome == nome


        def set_email(self, email):
            self._email == email
            
            


    def emitirCertificado(self):
        return print(f"\nCertificado do {self._nome} emitido com sucesso!")
    


class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso


    def emitirCertificado(self):
        return print(f"\nCertificado do {self._nome} concluiu o curso {self.curso}.")



class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade


    def emitirCertificado(self):
        return print(f"\nCertificado do {self._nome}, atuando como instrutor em {self.especialidade}.")
    




def main():

    participantes = []

    while True:
        print("\n====Cursos Online====\n")
        print("1. Cadastrar participante")
        print("2. Listar participante")
        print("3. Emitir certificados")
        print("4. Sair")
        opcao = input("\nDigite a opção que deseja (1-4): ")

        if opcao:
            if opcao == "1":
                print("\n-- Aluno")
                print("-- instrutor")
                info = input("Digite (A)luno ou (I)nstrutor: ").strip().upper()
                nome = input("Nome: ")
                email = input("Email: ")
                
                if info and nome and email:
                    if info == "A":
                        curso = input("Curso: ")
                        participantes.append(Aluno(nome, email, curso))
                    
                    elif info == "I":
                        especialidade = input("\nEspecialidade: ")
                        participantes.append(Instrutor(nome, email, especialidade))

                    else:
                        print("\nTipo inválido.")

                else:
                    print("\nOs campos não podem estar vazios.")

            elif opcao == "2":
                print("\n===Participantes cadastrados===\n")

                if not participantes:
                    print("\nNão há nenhum participante cadastrado.\n")

                else:
                    for p in participantes:
                        print(f"\n- {p._nome} ({p._email})")


            elif opcao == "3":
                print("\n===Certificados===\n")

                if not participantes:
                    print("\nNenhum certificado a emitir.\n")

                else:
                    for p in participantes:
                        print(p.emitirCertificado())


            elif opcao == "4":
                print("\nEncerrando o programa, até mais.\n")
                break

            else:
                print("\nOpção inválida.\n")




if __name__ == "__main__":
    main()