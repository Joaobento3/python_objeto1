'''n = quantidade de termos
   a1 = primeiro termo
   r = razão
   
   metodos: 
    calcular o n-ésimo termo (an)
    gerar todos o termos de P.A.
    calcular a soma dos termos (S)'''


class ProgressaoAritmetica:
    def __init__(self, n, a1, r):
        self.n = n
        self.a1 = a1
        self.r = r

    def calcular_termo(self):
        an = self.a1 + self.r * (self.n - 1)
        soma = self.n * (self.a1 + an) / 2
        return soma
    
    def gerar_termos(self):
        termos = []
        for i in range (self.n):
            termo = self.a1 + self.r * i
            termos.append(termo)
        return termos
    

def main():
    print("\n====Progressão Aritmética====\n")

    n = int(input("Digite o número de termos da P.A: "))
    a1 = float(input("Digite o primeiro termos (a1): "))
    r = float(input("Digite a razão (r): "))

    pa = ProgressaoAritmetica(n, a1, r)

    termos = pa.gerar_termos()

    print("\nTermos da P.A.: ")
    contador = 1
    for termo in termos:
        print(f"Termo {contador}: {termo}")
        contador += 1

    soma = pa.calcular_termo

    print(f"\nSoma dos {n} termos: {soma}\n")
        


if __name__ == "__main__":
    main()