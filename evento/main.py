from evento import Evento

def main():
    evento = Evento()

    while True:
        print("\nMenu:")
        print("1 - Inscrição")
        print("2 - Listar todos inscritos")
        print("3 - Entrar no evento")
        print("4 - Registro de saída")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            evento.inscricao()
        elif opcao == "2":
            evento.listar_inscritos()
        elif opcao == "3":
            evento.entrar_no_evento()
        elif opcao == "4":
            evento.registro_saida()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()