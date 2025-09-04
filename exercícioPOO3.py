class criptografiaTexto:
    def __init__(self, texto):
        self.texto = texto

    
    def criptografando(self):
        substituicoes = {
            "a":"4", "A":"4",
            "e":"3", "E":"3",
            "i":"1", "I": "1",
            "o":"0", "O": "0",
            "u":"8", "U": "8"
        }

        frase_criptografada = ""
        for caracter in self.texto:
            if caracter in substituicoes:
                frase_criptografada += substituicoes[caracter]
            else:
                frase_criptografada += caracter
        return frase_criptografada
    


def main():

    texto_usuario = input("\nDigite o texto que deseja criptografar: ")
    criptografador = criptografiaTexto(texto_usuario)
    resultado = criptografador.criptografando()
    print(f"\nFrase criptografada: {resultado}\n")





if __name__ == "__main__":
    main()