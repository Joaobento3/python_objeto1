class editorString:
    def __init__(self, string,):
     self.__string = string
    

    def numero_caracteres(self):
        return len (self.__string)


    def todas_maiusculo(self):
        return self.__string.upper()


    def todas_minusculo(self):
        return self.__string.lower()


    def numero_devogais(self):
        vogais = "aeiouAEIOU"
        contador = 0

        for caracter in self.__string:
            if caracter in vogais:
                contador += 1
        
        return contador
    

    def contem_ifb(self):
        return "IFB" in self.__string.upper()


def main():
    print("\n===Editor De String===\n")
    string = input("Digite a string que deseja editar: ")
    editor = editorString(string)
    
    print("\n===Análise do Texto===\n")
    print(f"Número de caracteres: {editor.numero_caracteres()}")
    print(f"Em maiúsculas: {editor.todas_maiusculo()}")
    print(f"Em minúculas: {editor.todas_minusculo()}")
    print(f"Número de vogais: {editor.numero_devogais()}")
    
    if editor.contem_ifb():
        print("A substring 'IFB' aparece no texto (independente de maiúsculas ou minúsculas)")
    else:
        print("A substring 'IFB' NÃO aparece no texto.")


if __name__ == "__main__":
    main()