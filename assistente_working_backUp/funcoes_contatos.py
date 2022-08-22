class ManipulaAgenda:
    _path: str
    _nome: str

    def __init__(self, path, nome):
        self._path = path
        self._nome = nome

    # CADASTRAR CONTATO
    def cadastrarContato(self):
        with open(self._path, "r", encoding="utf-8") as self._nome:
            idAutomatico = 1
            leitor = self._nome.read()
            linhaContato = leitor.split("\n")
            for linhas in linhaContato:
                if linhas:
                    idAutomatico += 1
                    self._nome.close()
            print(f'''
            --Cadastrando novo contato na Agenda: ''')
            nome = input("Escreva o Nome do Contato: ").capitalize()
            telefone = input("Escreva o número do telefone: ")
            email = input("Escreva o e-mail do Contato: ")
            dtNascimento = input("Escreva a data de nascimento: (dd/mm/aaaa) ")

        with open(self._path, "a", encoding="utf-8") as self._nome:
            dados = f'{idAutomatico};{nome};{telefone};{email};{dtNascimento}\n'
            self._nome.write(dados)
            self._nome.close()
            print(f'Contato gravado com sucesso!')

    # LISTAR TODOS OK
    def listarTodos(self):
        with open(self._path, "r", encoding="utf-8") as self._nome:
            for lista in self._nome:
                print(lista)

    # LISTAR CONTATO POR PESQUISA DE NOME, DDD, TELEFONE E E-MAIL | BUSCA POR DATA DE NASCIMENTO NÃO DEFINIDO
    def buscar(self):
        self.busca = input(f'''
    --(ex.: nome, DDD, telefone ou e-mail)
    >Digite a pesquisa: ''').capitalize()
        with open(self._path, "r", encoding="utf-8") as self._nome:
            for lista in self._nome:
                if self.busca in lista.split(';'):
                    print(
                        f'''
        >Nome: {lista.split(";")[1]}
        >Telefone: {lista.split(";")[2]} {lista.split(";")[3]}
        >E-mail: {lista.split(";")[4]}
        >Data de Nascimento: {lista.split(";")[5]}''')

    # DELETAR CADASTRO "r" = Leitura do arquivo | "a" = adiciona um novo conteúdo no fim do arquivo | "w" caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado
    def deletar(self):
        self.nome = input("Digite o nome a ser deletado: ")
        listatemp1 = []
        listatemp2 = []
        with open(self._path, "r", encoding="utf-8") as self._nome:
            verifica = input(f'''
Deseja realmente deletar {self.nome} da Agenda? (s/n) ''').lower()
            if verifica == "n":
                main()
            if verifica == "s":
                for i in self._nome:
                    listatemp1.append(i)
                for i in range(0, len(listatemp1)):
                    if self.nome not in listatemp1[i]:
                        listatemp2.append(listatemp1[i])
                with open(self._path, "w", encoding="utf-8") as self._nome:
                    for i in listatemp2:
                        self._nome.write(i)
                print("Contato deletado com sucesso!")
                self._nome.close()
            else:
                main()

    # ATUALIZAR CONTATO
    def atualizarContato(self):
        print(f'''
        --Atualização das informações de contato: ''')
        buscaAltera = input("Digite o nome do Contato a ser alterado: ")
        with open(self._path, "r", encoding="utf-8") as self._nome:
            for contatoUnico in self._nome:
                if buscaAltera in contatoUnico.split(";")[1]:
                    idAlt = contatoUnico.split(";")[0]
                    nomeAlt = contatoUnico.split(";")[1]
                    telefoneAlt = contatoUnico.split(";")[2]
                    emailAlt = contatoUnico.split(";")[3]
                    dtNascimentoAlt = contatoUnico.split(";")[4]
                    contatoAntigo = contatoUnico
                    print(f'Contato na agenda:', contatoUnico)

            verifica = input(f'Deseja realmente alterar o registro de {buscaAltera}? (s/n): ').lower()
            if verifica == "s":
                with open(self._path, "r", encoding="utf-8") as self._nome:
                    aux = []
                    aux2 = []
                    for i in self._nome:
                        aux.append(i)
                    for i in range(0, len(aux)):
                        if buscaAltera not in aux[i]:
                            aux2.append(aux[i])
                    with open(self._path, "w", encoding="utf-8") as self._nome:
                        for i in aux2:
                            self._nome.write(i)
                self._nome.close()
            else:
                main()
        # else:
        #     print(f'{buscaAltera} sem registro na agenda!')
        #     return

        altera = input("""
        ---Menu Alterações--
        [1] Alterar Nome
        [2] Alterar Telefone
        [3] Alterar E-mail
        [4] Alterar Data de Nascimento
        [5] Voltar ao Menu Principal
        ========================
        Escolha a opção acima: """)
        if altera == "1":
            novoNome = input("Digite o novo Nome: ")
            try:
                with open(self._path, "a", encoding="utf-8") as self._nome:
                    novoRegistro = f'{idAlt};{novoNome};{telefoneAlt};{emailAlt};{dtNascimentoAlt}'
                    self._nome.write(novoRegistro)
                    self._nome.close()
                    print("Contato alterado com sucesso!")
                    # chequemate
                    print("Registro antigo: ", contatoAntigo,
                          "Novo registro: ", novoRegistro)
            except:
                print(f'{buscaAltera} sem registro na agenda!')
        elif altera == "2":
            novoTelefone = input("Digite o novo telefone: ")
            try:
                with open(self._path, "a", encoding="utf-8") as self._nome:
                    novoRegistro = f'{idAlt};{nomeAlt};{novoTelefone};{emailAlt};{dtNascimentoAlt}'
                    self._nome.write(novoRegistro)
                    self._nome.close()
                    print("Contato alterado com sucesso!")
                    # chequemate
                    print("Registro antigo: ", contatoAntigo,
                          "Novo registro: ", novoRegistro)
            except:
                print(f'{buscaAltera} sem registro na agenda!')
        elif altera == "3":
            novoEmail = input("Digite o novo email: ")
            try:
                with open(self._path, "a", encoding="utf-8") as self._nome:
                    novoRegistro = f'{idAlt};{nomeAlt};{telefoneAlt};{novoEmail};{dtNascimentoAlt}'
                    self._nome.write(novoRegistro)
                    self._nome.close()
                    print("Contato alterado com sucesso!")
                    # chequemate
                    print("Registro antigo: ", contatoAntigo,
                          "Novo registro: ", novoRegistro)
            except:
                print(f'{buscaAltera} sem registro na agenda!')
        elif altera == "4":
            novoDtNacimento = input("Digite a data correta: (dd/mm/aaaa) ")
            try:
                with open(self._path, "a", encoding="utf-8") as self._nome:
                    novoRegistro = f'{idAlt};{nomeAlt};{telefoneAlt};{emailAlt};{novoDtNacimento}'
                    self._nome.write(novoRegistro)
                    self._nome.close()
                    # chequemate
                    print("Registro antigo: ", contatoAntigo, "\nNovo registro: ", novoRegistro)
            except:
                print(f'{buscaAltera} sem registro na agenda!')
        elif altera == "5":
            menu()
        else:
            print(f'Opção {altera} inválida!')
            main()

    # ENVIAR EMAIL
    def enviarEmail(self):
        import smtplib
        from email.message import EmailMessage
        emailUsuario = "agendapython.qroz@outlook.com"
        senhaUsuario = "@g3nd@python"
        try:
            smtpServer = smtplib.SMTP("smtp-mail.outlook.com", 587)
        except Exception as e:
            print(e)
            smtpServer = smtplib.SMTP_SSL("smtp-mail.outlook.com", 465)
        smtpServer.ehlo()
        smtpServer.starttls()

        emailBusca = input(f'''
        --Enviar e-mail
        Digite o nome do contato para enviar o e-mail: ''')
        with open(self._path, "r", encoding="utf-8") as self._nome:
            for contato in self._nome:
                if emailBusca in contato.split(";")[1]:
                    emailPara = contato.split(";")[4]
        try:
            msg = EmailMessage()
            msg["From"] = emailUsuario
            msg["To"] = emailPara
        except:
            op = input(f'''
            {emailBusca} sem registro na agenda!
            --O que deseja fazer?
            [1]Cadastrar {emailBusca}
            [2]Menu principal
            ========================
            Escolha uma opção acima: ''').lower()
            for opValida in ['1;2']:
                if op not in opValida.split(";"):
                    print(f'Opção {op} inválida!')
                    menu()
            if op == "1":
                self.cadastrarContato()
            if op == "2":
                menu()

        assunto = input("Digite o assunto do e-mail: ")
        corpoMensagem = input("Digite a mensagem a ser enviada: ")
        msg['Subject'] = assunto
        msg.set_content(corpoMensagem)

        # Enviar o E-mail

        try:
            smtpServer.login(emailUsuario, senhaUsuario)
            smtpServer.send_message(msg)
            print("E-mail enviado com sucesso!")
            return menu()
        except:
            print("E-mail não enviado!")
            menu()

# arquivo.cadastrarContato()
