import funcoes_contatos
import Cadastro_de_Tarefa
from assistente_working import dados_base_Agenda as db
import threading
# import Gerenciador_de_Alertas
versao_agenda = "AgendaPython 0.4.2"

def contadorID():
    agenda = open("agenda.txt","r", encoding="utf-8")
    marcadorID = 1
    leitor = agenda.read()
    linhaContato = leitor.split("\n")
    for linhas in linhaContato:
        if linhas:
            marcadorID += 1
            agenda.close()
            print(marcadorID)
#menu será a função principal do sistema
def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input(f'''
    {versao_agenda}
    --Menu Principal--
    [1]Cadastrar Contato
    [2]Listar Contato
    [3]Deletar Contato
    [4]Buscar Contato por Nome
    [5]Atualizar Contato
    [6]Enviar E-mail
    [7]Administrador de Tarefas
    [8]Sair
    ========================
    Escolha uma opção acima: ''')

        if opcao == "1":
            db.arquivoagenda.cadastrarContato()
        elif opcao == "2":
            db.arquivoagenda.listarTodos()
        elif opcao == "3":
            db.arquivoagenda.deletar()
        elif opcao == "4":
            db.arquivoagenda.buscar()
        elif opcao == "5":
            db.arquivoagenda.atualizarContato()
        elif opcao == "6":
            db.arquivoagenda.enviarEmail()
        elif opcao == "7":
            Cadastro_de_Tarefa.cadastrarTarefa()
        elif opcao == "8":
            sair()
        else:
            print("Opção incorreta!")
        voltarMenuPrincipal = input("Deseja voltar ao menu principal? (s/n): ").lower()
        if voltarMenuPrincipal == "n":
            sair()
        elif voltarMenuPrincipal == "s":
            menu()
        else:
            print(f'Opção {voltarMenuPrincipal} inválida para a operação!')
            menu()


def sair():
    print("Saída realizada, até mais..")
    exit()

def main():
    menu()
    # Gerenciador_de_Alertas()
    # threading.Thread(target=menu).start()
    # threading.Trhread(target=Gereciador_de_Alertas).start()
    # time.sleep(1)

main()
