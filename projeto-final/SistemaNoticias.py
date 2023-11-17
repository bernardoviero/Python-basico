import csv
from Noticia import Noticia

class SistemaNoticias:
    def __init__(self):
        self.noticias = []
        self.arquivo_csv = "noticias.csv"
        self.carregar_noticias()

    def cadastrar_noticia(self, noticia):
        self.noticias.append(noticia)
        self.salvar_noticias()

    def alterar_noticia(self, termo_pesquisa):
        noticia_encontrada = self.pesquisar_noticia(termo_pesquisa)
        if noticia_encontrada:
            novo_titulo = input("Novo titulo: ")
            nova_categoria = input("Nova categoria: ")
            novo_texto = input("Novo texto: ")
            novas_palavras_chave = input("Novas palavras chave (separadas por virgula): ").split(',')

            noticia_encontrada.titulo = novo_titulo
            noticia_encontrada.categoria = nova_categoria
            noticia_encontrada.texto = novo_texto
            noticia_encontrada.palavras_chave = novas_palavras_chave

            self.salvar_noticias()
            print("Noticia alterada com sucesso.")
        else:
            print("Notícia não encontrada.")

    def pesquisar_noticia(self, termo_pesquisa):
        for noticia in self.noticias:
            if termo_pesquisa.lower() in [noticia.titulo.lower(), noticia.categoria.lower(), noticia.texto.lower()] or \
                    termo_pesquisa.lower() in [palavra.lower() for palavra in noticia.palavras_chave]:
                return noticia
        return None

    def remover_noticia(self, termo_pesquisa):
        noticia_encontrada = self.pesquisar_noticia(termo_pesquisa)
        if noticia_encontrada:
            self.noticias.remove(noticia_encontrada)
            self.salvar_noticias()
            print("Notícia removida com sucesso.")
        else:
            print("Noticia não encontrada.")

    def salvar_noticias(self):
        with open(self.arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Título", "Categoria", "Texto", "Palavras chave"])
            for noticia in self.noticias:
                writer.writerow([noticia.titulo, noticia.categoria, noticia.texto, ','.join(noticia.palavras_chave)])

    def carregar_noticias(self):
        try:
            with open(self.arquivo_csv, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)
                for row in reader:
                    titulo, categoria, texto, palavras_chave = row
                    palavras_chave = palavras_chave.split(',')
                    noticia = Noticia(titulo, categoria, texto, palavras_chave)
                    self.noticias.append(noticia)
        except FileNotFoundError:
            self.salvar_noticias()