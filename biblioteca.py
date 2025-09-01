def main():
    livro1 = Livro("Harry Potter", "J. K. Rolling", 1)
    livro2 = Livro("Jogos Vorazes", "Susan Colling", 2)
    livro3 = Livro("Dom Casmurro", "Machado de Assis", 3)

    usuario1 = Usuario("Marcos", 659875)

    usuario1.emprestar_livros(livro1)
    usuario1.emprestar_livro(livro2)

    usuario1.listar_livros_emprestados()

    usuario1.devolver_livro(2)

    usuario1.listar_livros_emprestados
    



if __name__ == "__main__":
    main()