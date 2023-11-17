from SistemaNoticias import SistemaNoticias
from Noticia import Noticia

class Main:
    def __init__(self):
        self.sistema = SistemaNoticias()

    def menu_principal(self):
        while True:
            print("\nOpções:")
            print("1 - Cadastrar Notícia")
            print("2 - Alterar Notícia")
            print("3 - Pesquisar Notícia")
            print("4 - Remover Notícia")
            print("0 - Sair")

            escolha = input("Escolha a opção: ")

            if escolha == "1":
                titulo = input("Título: ")
                categoria = input("Categoria: ")
                texto = input("Texto: ")
                palavras_chave = input("Palavras-chave (separadas por vírgula): ").split(',')

                noticia = Noticia(titulo, categoria, texto, palavras_chave)
                self.sistema.cadastrar_noticia(noticia)

            elif escolha == "2":
                termo_pesquisa = input("Digite o título, categoria, texto ou palavras-chave da notícia que deseja alterar: ")
                self.sistema.alterar_noticia(termo_pesquisa)

            elif escolha == "3":
                termo_pesquisa = input("Digite o título, categoria, texto ou palavras-chave da notícia que deseja pesquisar: ")
                noticia_encontrada = self.sistema.pesquisar_noticia(termo_pesquisa)
                if noticia_encontrada:
                    print(f"\nNotícia encontrada:")
                    print(f"Título: {noticia_encontrada.titulo}")
                    print(f"Categoria: {noticia_encontrada.categoria}")
                    print(f"Texto: {noticia_encontrada.texto}")
                    print(f"Palavras-chave: {', '.join(noticia_encontrada.palavras_chave)}")
                else:
                    print("Notícia não encontrada.")

            elif escolha == "4":
                termo_pesquisa = input("Digite o título, categoria, texto ou palavras-chave da notícia que deseja remover: ")
                self.sistema.remover_noticia(termo_pesquisa)

            elif escolha == "0":
                self.sistema.salvar_noticias()
                print("Saindo do sistema!")
                break

            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    gerenciador = Main()
    gerenciador.menu_principal()