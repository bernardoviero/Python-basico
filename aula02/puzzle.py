import random

class Puzzle:
    def __init__(self, dimensao, op=None):
        self.matriz = [[0 for _ in range(dimensao)] for _ in range(dimensao)]
        self.dimensao = dimensao
        self.linha = 0
        self.coluna = 0
        self.op = op
        
        lista = list(range(dimensao * dimensao))
        random.shuffle(lista)
        posicao = 0
        
        for i in range(dimensao):
            for j in range(dimensao):
                self.matriz[i][j] = lista[posicao]
                if self.matriz[i][j] == 0:
                    self.linha = i
                    self.coluna = j
                posicao += 1

    def getDescricao(self):
        return "Problema do Puzzle de NxN"

    def ehMeta(self):
        posicao = 0
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                if self.matriz[i][j] != posicao:
                    return False
                posicao += 1
        return True

    def custo(self):
        return 1

    def sucessores(self):
        visitados = []

        self.cima(visitados)
        self.baixo(visitados)
        self.esquerda(visitados)
        self.direita(visitados)

        return visitados

    def clonar(self):
        matriz_tmp = [[0 for _ in range(self.dimensao)] for _ in range(self.dimensao)]
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                matriz_tmp[i][j] = self.matriz[i][j]
        return matriz_tmp

    def cima(self, visitados):
        if self.linha == 0:
            return

        matriz_tmp = self.clonar()

        matriz_tmp[self.linha][self.coluna] = matriz_tmp[self.linha - 1][self.coluna]
        matriz_tmp[self.linha - 1][self.coluna] = 0

        novo = Puzzle(matriz_tmp, self.linha - 1, self.coluna, "Indo para cima")
        if novo not in visitados:
            visitados.append(novo)
        else:
            print("visitado....")

    def baixo(self, visitados):
        if self.linha == self.dimensao - 1:
            return

        matriz_tmp = self.clonar()

        matriz_tmp[self.linha][self.coluna] = matriz_tmp[self.linha + 1][self.coluna]
        matriz_tmp[self.linha + 1][self.coluna] = 0

        novo = Puzzle(matriz_tmp, self.linha + 1, self.coluna, "Indo para baixo")
        if novo not in visitados:
            visitados.append(novo)
        else:
            print("visitado....")

    def esquerda(self, visitados):
        if self.coluna == 0:
            return

        matriz_tmp = self.clonar()

        matriz_tmp[self.linha][self.coluna] = matriz_tmp[self.linha][self.coluna - 1]
        matriz_tmp[self.linha][self.coluna - 1] = 0

        novo = Puzzle(matriz_tmp, self.linha, self.coluna - 1, "Indo para esquerda")
        if novo not in visitados:
            visitados.append(novo)
        else:
            print("visitado....")

    def direita(self, visitados):
        if self.coluna == self.dimensao - 1:
            return

        matriz_tmp = self.clonar()

        matriz_tmp[self.linha][self.coluna] = matriz_tmp[self.linha][self.coluna + 1]
        matriz_tmp[self.linha][self.coluna + 1] = 0

        novo = Puzzle(matriz_tmp, self.linha, self.coluna + 1, "Indo para direita")
        if novo not in visitados:
            visitados.append(novo)
        else:
            print("visitado....")

    def __eq__(self, other):
        if isinstance(other, Puzzle):
            for i in range(self.dimensao):
                for j in range(self.dimensao):
                    if other.matriz[i][j] != self.matriz[i][j]:
                        return False
            return True
        return False

    def __str__(self):
        resposta = []
        resposta.append(self.op + "\n")
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                resposta.append(str(self.matriz[i][j]) + " ")
            resposta.append("\n")
        resposta.append("Posicao do 0: " + str(self.linha) + "," + str(self.coluna) + "\n\n")
        return ''.join(resposta)

    def __hash__(self):
        estado = ""

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                estado = estado + str(self.matriz[i][j])

        return hash(estado)

dimensao = int(input("Entre com a dimensao: "))
estadoInicial = Puzzle(dimensao, "Estado Inicial")

#PARTE DO JAVA QUE VAMOS IMPLEMENTAR NA PRÓXIMA AULA
#   Nodo n = new BuscaLargura(new MostraStatusConsole()).busca(estadoInicial);
        
# if n == null:
#     print("sem solução")
# else:
#     print("solução = "+n.montaCaminho())