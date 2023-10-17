# criar uma menu para cadastro, listagem e pesquisa de receitas
# salvar essas receitas em uma lista
# essa lista deve ser salva em um arquivo .CSV
# começar salvando apenas o titulo da receita, e nas próximas aulas salvaremos os ingredientes, modo de preparo e tipo de receita(doce ou salgada).

from util import cadastrar, listar, pesquisar

lista_receitas = []

while (True):
  print('MENU')
  print('1 - Cadastrar Receita')
  print('2 - Listar Receitas')
  print('3 - Pesquisar por Receita')
  print('4 - Finalizar')
  opcao = input('Opções: ')

  if opcao == '1':
    print('Cadastrar')
    #chamar o metodo de cadastro
    cadastrar(lista_receitas)
  elif opcao == '2':
    print('Listagem de Receitas')
    #chamar o metodo de listagem
    listar()
  elif opcao == '3':
    receita = input('Pesquisa: ')
    #chamar o metodo de pesquisa de receitas
    pesquisar(receita.upper())
  elif opcao == '4':
    print('Obrigado por usar o sistema')
    break
  else:
    print('Opção inválida!')
