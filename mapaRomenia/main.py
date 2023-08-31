class Cidade:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Grafo:
    def __init__(self):
        self.cidades = []
        self.matriz_adjacencia = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)
        num_cidades = len(self.cidades)
        for linha in self.matriz_adjacencia:
            linha.append(0)
        self.matriz_adjacencia.append([0] * num_cidades)

    def adicionar_distancia(self, cidade1, cidade2, distancia):
        indice_cidade1 = self.cidades.index(cidade1)
        indice_cidade2 = self.cidades.index(cidade2)
        self.matriz_adjacencia[indice_cidade1][indice_cidade2] = distancia
        self.matriz_adjacencia[indice_cidade2][indice_cidade1] = distancia

    def imprimir_matriz_adjacencia(self):
        for linha in self.matriz_adjacencia:
            print(' '.join(map(str, linha)))


def main():
    grafo = Grafo()

    arquivo = 'mapaRomenia.txt'
    with open(arquivo, 'r') as f:
        for linha in f:
            cidade1, cidade2, distancia = linha.strip().split('@')
            if cidade1 not in grafo.cidades:
                grafo.adicionar_cidade(cidade1)
            if cidade2 not in grafo.cidades:
                grafo.adicionar_cidade(cidade2)
            grafo.adicionar_distancia(cidade1, cidade2, int(distancia))

    grafo.imprimir_matriz_adjacencia()


if __name__ == "__main__":
    main()
