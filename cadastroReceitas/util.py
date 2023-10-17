import csv


def cadastrar(lista):
  titulo = input('Informe o título da Receita: ')
  retorno, mensagem = pesquisar(titulo)
  if titulo in lista or retorno == 0:
    print('Esta Receita já foi cadastrada!')
  else:
    try:
      lista.append(titulo)
      titulo = titulo.upper()
      escritor = open('receitas.csv', 'a')
      escritor.write(titulo + '\n')
      escritor.close()
      print("Receita cadastrada!")
    except:
      print("Erro ao cadastrar Receita\n")


def listar():
  try:
    with open('receitas.csv', 'r', encoding='utf-8') as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)
      for linha in leitor_csv:
        print(linha)
  except:
    print('Sem receitas até o momento\n')


def pesquisar(titulo):
  try:
    with open('receitas.csv', 'r', encoding='utf-8') as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)
      resultados = []
      for linha in leitor_csv:
        if titulo in linha[0]:
          resultados.append(linha)
      if resultados:
        for resultado in resultados:
          print(resultado)
      else:
        return 0, "Não existe uma Receita com esse título"
  except FileNotFoundError:
    print('Não foi possível encontrar o arquivo.')
