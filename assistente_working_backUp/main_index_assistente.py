import funcoes_contatos
import Cadastro_de_Tarefa
from assistente_working import dados_base_Agenda as db
import threading
# import Gerenciador_de_Alertas
versao_agenda = "AgendaPython 0.4.2"
# def cadastrarTarefa():
#     opTar = input(f'''
#     {versao_agenda}
#     --Administrador de Tarefa--
#
#     [1]Nova - testado
#     [2]Deletar - não resolvido
#     [3]Editar - não resolvido
#     [4]Buscar tarefa - testado com obs
#     [5]Voltar - testado
#     ========================
#     Escolha uma opção acima: ''')
#     for opValida in ['1;2;3;4;5']:
#         if opTar not in opValida.split(";"):
#             print(f'Opção {opTar} inválida!')
#             cadastrarTarefa()
#     # CADASTRAR TAREFA - OK
#     if opTar == "1":
#         perguntaRepete = input('''
#             --Configuração de alerta:
#             [1]Por data específica
#             [2]Repetição
#             [3]Voltar
#             ========================
#             Escolha uma opção acima: ''')
#         for opValida in ['1;2;3']:
#             if perguntaRepete not in opValida.split(";"):
#                 print(f'Opção {perguntaRepete} inválida!')
#                 cadastrarTarefa()
#         if perguntaRepete == "1":
#             dtTarefa = input("Data de execução: (DD/MM/AAAA)").time.strftime('%d/%m/%Y', time.localtime())
#             tituloTarefa = input("Nomeie a tarefa: ").upper()
#             hrTarefa = input("Hora da execução: (HH:MM)")
#             classificacao = "1"
#             repete = "0"
#             textoTarefa = input("Digite a Mensagem: ")
#             try:
#                 with open("listaTarefa.txt", "a", encoding="utf-8") as listadeTarefa:
#                     novaTarefa = f'{tituloTarefa};{classificacao};{dtTarefa};{hrTarefa};{repete};{textoTarefa}\n'
#                     listadeTarefa.write(novaTarefa)
#                     listadeTarefa.close()
#                     print(f'Tarefa {tituloTarefa} adicionada com SUCESSO!')
#             except:
#                 print(f'Tarefa {tituloTarefa} NÃO adicionada!')
#                 cadastrarTarefa()
#         if perguntaRepete == "2":
#             repete = input('''
#             --Repetição da tarefa:
#                 Digite os dias da repição separados por /
#             [1]Domingo
#             [2]Segunda
#             [3]Terça
#             [4]Quarta
#             [5]Quinta
#             [6]Sexta
#             [7]Sábado
#             [8]Todos os dias
#             ========================
#             Escolha uma opção acima: ''')
#             for opValida in ['1;2;3;4;5;6;7;8']:
#                 if repete not in opValida.split(";"):
#                     print(f'Opção inválida!')
#                     cadastrarTarefa()
#             tituloTarefa = input("Nomeie a tarefa: ").upper()
#             hrTarefa = input("Hora da execução: (HH:MM)")
#             classificacao = "1"
#             dtTarefa = "00/00/0000"
#             textoTarefa = input("Digite a Mensagem: ")
#             try:
#                 with open("listaTarefa.txt", "a", encoding="utf-8") as listadeTarefa:
#                     novaTarefa = f'{tituloTarefa};{classificacao};{dtTarefa};{hrTarefa};{repete};{textoTarefa}\n'
#                     listadeTarefa.write(novaTarefa)
#                     listadeTarefa.close()
#                     print(f'Tarefa {tituloTarefa} adicionada com SUCESSO!')
#                     cadastrarTarefa()
#             except:
#                 print(f'Tarefa {tituloTarefa} NÃO adicionada!')
#         if perguntaRepete == "3":
#             cadastrarTarefa()
#     # DELETAR TAREFA
#     elif opTar == "2":
#         print("Deletar Tarefa")
#     # EDITAR TAREFA
#     elif opTar == "3":
#         print("Editar Tarefa")
#     # BUSCAR TAREFA - <<busca por data>> com observação as demais opções estão resolvidas
#     elif opTar == "4":
#         op = input(f'''
#             --Buscar tarefa:
#             [1]Todas as tarefas
#             [2]Por Nome
#             [3]Por Data
#             [4]Por Classificação
#             [5]Voltar
#             ========================
#             Escolha uma opção acima: ''')
#         for opValida in ['1;2;3;4;5']:
#             if op not in opValida.split(";"):
#                 print(f'Opção {op} inválida!')
#                 cadastrarTarefa()
#         # BUSCAR TODAS - OK
#         if op == "1":
#             with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                 for tarefa in listaTarefa:
#                     print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                 listaTarefa.close()
#         # BUSCA POR NOME - OK
#         elif op == "2":
#             busca = input("Digite o nome da tarefa: ").upper()
#             with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                 for tarefa in listaTarefa:
#                     if busca in tarefa.split(";")[0]:
#                         print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                     elif busca not in tarefa.split(";")[0]:
#                         print("Tarefa não encontrada!")
#                         cadastrarTarefa()
#                 listaTarefa.close()
#         # BUSCA POR DATA - com OBSERVAÇÂO
#         elif op == "3":
#             busca = input('''
#             --Buscar tarefa > por data:
#             [1]Data completa: (DD/MM/AAAA)
#             [2]Dia: (DD)
#             [3]Mês: (MM)
#             [4]Ano:(AAAA)
#             [5]Voltar
#             ========================
#             Escolha uma opção acima: ''')
#             for opValida in ['1;2;3;4;5']:
#                 if busca not in opValida.split(";"):
#                     print(f'Opção {busca} inválida!')
#                     cadastrarTarefa()
#             # BUSCA POR DATA COMPLETA - OK FUNCIONANDO
#             if busca == "1":
#                 buscaop2 = input("Digite a Data: (DD/MM/AAA)  ")
#                 with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                     for tarefa in listaTarefa:
#                         if buscaop2 in tarefa.split(";")[2]:
#                             print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                     listaTarefa.close()
#             # BUSCA POR DATA SUBMENU BUSCA POR DIA - é buscando o valor inserido na string dataBusca inteira tem que buscar apenas o dia
#             elif busca == "2":
#                 buscaop2 = input("Digite o Dia: (DD)  ")
#                 with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                     for tarefa in listaTarefa:
#                         if buscaop2 in tarefa.split(";")[2]:
#                             dataBusca = tarefa.split("/")[0]
#                             print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                     listaTarefa.close()
#             # BUSCA POR DATA SUBMENU BUSCA POR MÊS - é buscando o valor inserido na string dataBusca inteira tem buscar apenas o mês
#             elif busca == "3":
#                 buscaop2 = input("Digite o Dia: (MM)  ")
#                 with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                     for tarefa in listaTarefa:
#                         if buscaop2 in tarefa.split(";")[2]:
#                             dataBusca = tarefa.split("/")[1]
#                             print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                     listaTarefa.close()
#             # BUSCA POR DATA SUBMENU BUSCA POR ANO - é buscando o valor inserido na string dataBusca inteiratem que buscar apenas o ano
#             elif busca == "4":
#                 buscaop2 = input("Digite o Dia: (AAAA)  ")
#                 with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                     for tarefa in listaTarefa:
#                         if buscaop2 in tarefa.split(";")[2]:
#                             dataBusca = tarefa.split("/")[1]
#                             print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                     listaTarefa.close()
#             elif busca =="5":
#                 cadastrarTarefa()
#         # BUSCA POR CLASSIFICAÇÃO - OK
#         elif op == "4":
#             busca = input('''
#             --Buscar tarefa > por classificação:
#             [1]Baixa
#             [2]Média
#             [3]Alta
#             ========================
#             Escolha uma opção acima: ''')
#             for opValida in ['1;2;3']:
#                 if busca not in opValida.split(";"):
#                     print(f'Opção {busca} inválida!')
#                     cadastrarTarefa()
#             with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
#                 for tarefa in listaTarefa:
#                     if busca in tarefa.split(";")[1]:
#                         print(f'''
#     Título: {tarefa.split(";")[0]}
#     Classificação: {tarefa.split(";")[1]}
#     Data de execução: {tarefa.split(";")[2]}
#     Hora de execução: {tarefa.split(";")[3]}
#     Repetição: {tarefa.split(";")[4]}
#     Descritivo/Mensagem: {tarefa.split(";")[5]}''')
#                 listaTarefa.close()
#     elif opTar == "5":
#         menu()

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