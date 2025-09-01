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

    def calcular_termo(self, k):
        return self.a1 + self.r * (k - 1)
    
    def gerar_termos(self):
        return [self.calcular_termo(i) for i in range (1, self.n + 1)]
    
    def soma(self):
        an = self.calcular_termo(self.n)
        return self.n * (self.a1 + an) / 2
    

def main():
    n = int(input("\nDigite o número de termos da P.A: "))
    a1 = int(input("Digite o primeiro termos (a1): "))
    r = int(input("Digite a razão (r): "))

    pa = ProgressaoAritmetica(n, a1, r)

    termos = pa.gerar_termos()
    print("\nTermos da P.A.:", termos)
    print("Soma dos termos:", pa.soma())
        


if __name__ == "__main__":
    main()