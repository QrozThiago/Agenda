
def cadastrarTarefa():
    opTar = input(f'''
    --Administrador de Tarefa--
    [1]Nova - testado
    [2]Deletar - não resolvido
    [3]Editar - não resolvido
    [4]Buscar tarefa - testado com obs
    [5]Voltar - testado
    ========================
    Escolha uma opção acima: ''')
    # CADASTRAR TAREFA - OK
    if opTar == "1":
        perguntaRepete = input('''
            --Configuração de alerta:
            [1]Por data específica
            [2]Repetição
            ========================
            Escolha uma opção acima: ''')
        if perguntaRepete == "1":
            dtTarefa = input("Data de execução: (DD/MM/AAAA)")
            tituloTarefa = input("Nomeie a tarefa: ").upper()
            hrTarefa = input("Hora da execução: (HH:MM)")
            classificacao = "1"
            repete = "0"
            textoTarefa = input("Digite a Mensagem: ")
            try:
                with open("listaTarefa.txt", "a", encoding="utf-8") as listadeTarefa:
                    novaTarefa = f'{tituloTarefa};{classificacao};{dtTarefa};{hrTarefa};{repete};{textoTarefa}\n'
                    listadeTarefa.write(novaTarefa)
                    listadeTarefa.close()
                    print(f'Tarefa {tituloTarefa} adicionada com SUCESSO!')
            except:
                print(f'Tarefa {tituloTarefa} NÃO adicionada!')
        elif perguntaRepete == "2":
            repete = input('''
            --Repetição da tarefa:
                Digite os dias da repição separados por /
            [1]Domingo
            [2]Segunda
            [3]Terça
            [4]Quarta
            [5]Quinta
            [6]Sexta
            [7]Sábado
            [8]Todos os dias
            ========================
            Escolha uma opção acima: ''')
            tituloTarefa = input("Nomeie a tarefa: ").upper()
            hrTarefa = input("Hora da execução: (HH:MM)")
            classificacao = "1"
            dtTarefa = "00/00/0000"
            textoTarefa = input("Digite a Mensagem: ")
            try:
                with open("listaTarefa.txt", "a", encoding="utf-8") as listadeTarefa:
                    novaTarefa = f'{tituloTarefa};{classificacao};{dtTarefa};{hrTarefa};{repete};{textoTarefa}\n'
                    listadeTarefa.write(novaTarefa)
                    listadeTarefa.close()
                    print(f'Tarefa {tituloTarefa} adicionada com SUCESSO!')
            except:
                print(f'Tarefa {tituloTarefa} NÃO adicionada!')
            else:
                return cadastrarTarefa()
    # DELETAR TAREFA
    elif opTar == "2":
        print("Deletar Tarefa")
    # EDITAR TAREFA
    elif opTar == "3":
        print("Editar Tarefa")
    # BUSCAR TAREFA - <<busca por data>> com observação as demais opções estão resolvidas
    elif opTar == "4":
        op = input(f'''
    [1]Buscar todas as tarefas
    [2]Buscar tarefa por nome
    [3]Buscar tarefa por data
    [4]Buscar tarefa por classificação
    ========================
    Escolha uma opção acima: ''')
        # BUSCAR TODAS - OK
        if op == "1":
            with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                for tarefa in listaTarefa:
                    print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                listaTarefa.close()
        # BUSCA POR NOME - OK
        elif op == "2":
            busca = input("Digite o nome da tarefa: ").upper()
            with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                for tarefa in listaTarefa:
                    if busca in tarefa.split(";")[0]:
                        print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                listaTarefa.close()
        # BUSCA POR DATA - com OBSERVAÇÂO
        elif op == "3":
            busca = input('''
    [1]Data completa: (DD/MM/AAAA) 
    [2]Dia: (DD) 
    [3]Mês: (MM) 
    [4]Ano:(AAAA)
    ========================
    Escolha uma opção acima: ''')
            # BUSCA POR DATA COMPLETA - OK FUNCIONANDO
            if busca == "1":
                buscaop2 = input("Digite a Data: (DD/MM/AAA)  ")
                with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                    for tarefa in listaTarefa:
                        if buscaop2 in tarefa.split(";")[2]:
                            print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                    listaTarefa.close()
            # BUSCA POR DATA SUBMENU BUSCA POR DIA - é buscando o valor inserido na string dataBusca inteira tem que buscar apenas o dia
            elif busca == "2":
                buscaop2 = input("Digite o Dia: (DD)  ")
                with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                    for tarefa in listaTarefa:
                        if buscaop2 in tarefa.split(";")[2]:
                            dataBusca = tarefa.split("/")[0]
                            print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                    listaTarefa.close()
            # BUSCA POR DATA SUBMENU BUSCA POR MÊS - é buscando o valor inserido na string dataBusca inteira tem buscar apenas o mês
            elif busca == "3":
                buscaop2 = input("Digite o Dia: (MM)  ")
                with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                    for tarefa in listaTarefa:
                        if buscaop2 in tarefa.split(";")[2]:
                            dataBusca = tarefa.split("/")[1]
                            print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                    listaTarefa.close()
            # BUSCA POR DATA SUBMENU BUSCA POR ANO - é buscando o valor inserido na string dataBusca inteiratem que buscar apenas o ano
            elif busca == "4":
                buscaop2 = input("Digite o Dia: (AAAA)  ")
                with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                    for tarefa in listaTarefa:
                        if buscaop2 in tarefa.split(";")[2]:
                            dataBusca = tarefa.split("/")[1]
                            print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                    listaTarefa.close()
        # BUSCA POR CLASSIFICAÇÃO - OK
        elif op == "4":
            busca = input('''
    [1]Baixa
    [2]Média
    [3]Alta
    ========================
    Escolha uma opção acima: ''')
            with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefa:
                for tarefa in listaTarefa:
                    if busca in tarefa.split(";")[1]:
                        print(f'''
    Título: {tarefa.split(";")[0]}
    Classificação: {tarefa.split(";")[1]}
    Data de execução: {tarefa.split(";")[2]}
    Hora de execução: {tarefa.split(";")[3]}
    Repetição: {tarefa.split(";")[4]}
    Descritivo/Mensagem: {tarefa.split(";")[5]}''')
                listaTarefa.close()
    if opTar == "5":
        return menu()
