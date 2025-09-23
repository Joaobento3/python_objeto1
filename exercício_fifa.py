from abc import ABC, abstractmethod

class ClubeParticipante(ABC):
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias


    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"País: {self.pais}")
        print(f"Confederação: {self.confederacao}")
        print(f"Ranking fifa: {self.ranking_fifa}")
        print(f"Gols marcados: {self.gols_marcados}")
        print(f"Vitórias: {self.vitorias}")


    @abstractmethod
    def calcular_desempenho(self):
        pass


    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass



class ClubeUEFA(ClubeParticipante):
    def calcular_desempenho(self):
        return self.vitorias * 3 + self.gols_marcados * 0.5
    

    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        print(f"Desempenho UEFA: {desempenho}")



class ClubeCONMEBOL(ClubeParticipante):
    def calcular_desempenho(self):
        return self.vitorias * 3 + self.gols_marcados * 0.7
    

    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        print(f"Desempenho CONMEBOL: {desempenho}")



def main():
    
    clube1 = ClubeUEFA("Real Madrid", "Espanha", "UEFA", 1, 10, 3)
    clube2 =   ClubeCONMEBOL("Palmeiras", "Brasil", "CONMEBOL", 5, 8, 2) 

    clubes = [clube1, clube2]

    for clube in clubes:
        clube.gerar_relatorio_tecnico()
        print("-" * 30)





if __name__ == "__main__":
    main()