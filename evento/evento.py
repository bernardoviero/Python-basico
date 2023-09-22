import datetime
from participante import Participante

class Evento:
    def __init__(self):
        self.participantes = []
        self.inscritos = set()
        self.entradas = []
        self.saidas = []

        self.carregar_inscricoes()

    def inscricao(self):
        matricula = input("Digite a matrícula: ")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")

        if email in self.inscritos:
            print("Este email já está inscrito no evento.")
        else:
            participante = Participante(matricula, nome, email)
            self.participantes.append(participante)
            self.inscritos.add(email)
            with open("inscricoes.dat", "a") as arquivo:
                arquivo.write(f"{matricula};{nome};{email}\n")
            print("Inscrição realizada com sucesso!")

    def listar_inscritos(self):
        print("Lista de Inscritos:")
        for participante in self.participantes:
            print(f"Matrícula: {participante.matricula}, Nome: {participante.nome}, Email: {participante.email}")

    def carregar_inscricoes(self):
        try:
            with open("inscricoes.dat", "r") as arquivo:
                for linha in arquivo:
                    matricula, nome, email = linha.strip().split(";")
                    participante = Participante(matricula, nome, email)
                    self.participantes.append(participante)
                    self.inscritos.add(email)
        except FileNotFoundError:
            pass 

    def entrar_no_evento(self):
        matricula = input("Digite a matrícula para entrada: ")
        for participante in self.participantes:
            if participante.matricula == matricula:
                hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.entradas.append(f"{matricula};{hora_atual}")
                with open("entradas.dat", "a") as arquivo:
                    arquivo.write(f"{matricula};{hora_atual}\n")
                print("Entrada registrada com sucesso!")
                return
        print("Matrícula não encontrada. Entrada não registrada.")

    def registro_saida(self):
        matricula = input("Digite a matrícula para saída: ")
        for participante in self.participantes:
            if participante.matricula == matricula:
                hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.saidas.append(f"{matricula};{hora_atual}")
                with open("saidas.dat", "a") as arquivo:
                    arquivo.write(f"{matricula};{hora_atual}\n")
                print("Saída registrada com sucesso!")
                return
        print("Matrícula não encontrada. Saída não registrada.")