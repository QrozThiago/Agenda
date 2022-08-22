--> Arquivo ReadMe.txt
Projeto de estudo a partir do vídeo (https://www.youtube.com/watch?v=kuuX6jzHg-M&ab_channel=ThalesVeloso).
#######----------#######----------#######

Projeto original:
    Agenda de contatos com base de dados em .txt com as informações de ID, Nome, Telefone, Email.
    Funções:
        -Cadastrar novo contato (inserir todas as informações do contato manualmente);
        -Listar todos os cotatos da Agenda.txt;
        -Deletar contato buscando pelo Nome;
        -Exibir informações de um único contato (busca por Nome com input() de texto);
        -Atualizar informações de um contato único (busca por Nome com input() de texto);
        -Sair da Agenda
Objetivo:
    Automatizar agenda:
        -Implantar recursos de interação com o usuário;
        -Reconhecer comandos de input() por voz;
            .Referência - https://www.youtube.com/watch?v=36RIoJeV95M&ab_channel=Codifike
        -Salvar informações em BD;
        -Recurso de print() por voz do programa;


#######----------#######----------#######

V0.1
    Dinâmica de input() melhorada;
    Automatização o ID do contato ainda não funcionando;
V0.2
    Automatização do ID de contato funcionando;
    Limpeza de linhas vazias - Não funcionando;
    Melhorias na atualização do contato:
        -Possibilita o usuário a alterar a informação do contato escolhida por input().
        -Bug pular linha ao fazer a atualização - Não resolvido;
V0.3
    Criar informação de data de nascimento - Concluído;
    Limpeza de linhas vazias - Não funcionando;
    Bug pular linha ao fazer atualização do contato - Concluído;
    Enviar email - Função funcionando
        ->E-mail usuário da agenda: agendapython.qroz@outlook.com
        -Contas cadastradas:
            .Usuário e-mail: agendapython.qroz@gmail.com
            .Senha: @g3nd@python
            .Usuário e-mail: agendapython.qroz@outlook.com
            .Senha: @g3nd@python
        -Pendências:
            .Bloquear tentativa de envio para contato fora da agenda - Concluído;
                ..(Aconteceu algum erro e não consegui recuperar a versão. Programar novamente.)
            .(desativado temporariamente) Fução de retorno para novo e-mail - funcioando sem pergunta ao usuário;
    Enviar lembrete de aniversário - Não resolvido; (A partir da versão 0.3.1 será chamado de - Gerenciador de Tarefas)
        -Testar: https://acervolima.com/aplicativo-de-lembrete-de-aniversario-em-python/
    Mensagem de erro:
        -Escolher opção inválida no Menu Principal - OK;
        -Escolher opção inválida no Menu Alterações - OK;
        -Buscar contato por nome - Volta ao menu() - OK com mensagem paleativa de informação não encontrada;
        -Entar atualizar um contato sem registro na AgendaPython resolvido com try: e except: ao gravar no arquivo agenda.txt

V0.3.1
    Criada versão de segurança 0.3.1 para envio de e-mail. Ajustado o bloqueio de envio de email a contato sem registro na agenda. Versão 0.3 com o código inicial da versão 0.3.1.

V0.4
    Limpeza de linhas vazias - Não funcionando;
    Gerenciador de tarefas - Em processo de desenvolvimento;
        -Criar recursos para cadastro de tarefas - OK;
        -Referência CÓDIGO RODADO COM O WINDOWS DESLIGADO
            https://www.youtube.com/watch?v=-Wro4N9qWEQ&ab_channel=HashtagPrograma%C3%A7%C3%A3o
        -Referência: https://www.youtube.com/watch?v=XMATWbPNems&ab_channel=pythonando
        -Testar: https://acervolima.com/aplicativo-de-lembrete-de-aniversario-em-python/
        -Funções do gerenciador:
            ..Nova
                ..Tarefa Diária
                ..Tarefa Agendada
            ..Deletar
            ..Editar
            ..Buscar tarefa
                ..Listar Tarefas
                ..Exibir Tarefa selecionada
                    ...Por Título
                    ...Por Data
                        ....Data completa
                        ....Dia
                        ....Mês
                        ....Ano
                    ...Por Hora
                        ....Escolhida pelo usuário
                        ....Manhã
                        ....Tarde
                        ....Noite
                    ...Por Classificação
                        ....Baixa
                        ....Média
                        ....Alta
                ..Tarefas concluídas
                ..Tarefas pendentes
                ..
            ..Voltar
    Notificação no Windows - Funcionando - Definir alertas programados com recorrencia;
        -Referência -https://www.youtube.com/watch?v=p1w-FZclhXs&ab_channel=Nexus-Stack
                    -https://www.youtube.com/watch?v=1dqeOEXDkrM&ab_channel=RishabhNarayan
                    -https://www.youtube.com/watch?v=PAnrHMQBB-Y&ab_channel=DevAprender
    Enviar mensagem programada para o Whatsapp - Não resolvido;
        -Referência - https://www.youtube.com/watch?v=UenvIUxYo-0&ab_channel=DevAprender
        -Referência - https://www.youtube.com/watch?v=Ii0TCI_FP48&ab_channel=DevAprender
    AgendaPython como programa executável .exe - Executando, Funcionando; Problema com o .exe com comandos de tarefas;
        -Referênciaa - https://www.youtube.com/watch?v=TBdRfrWT7Co&ab_channel=DevAprender
        -Referência - https://www.youtube.com/watch?v=Ii0TCI_FP48&ab_channel=DevAprender
        -Referência - https://stackoverflow.com/questions/57378765/runtimeerror-cx-freeze-freezer-configerror-cannot-find-file-directory-named-n
        -Criada pasta -output- para arquivos e testes de execução. Nome do arquivo da agenda renomeado para -AgendaPython V0-4 Beta- na pasta -output-;
    Sistema de login com e-mail OUTLOOK e SENHA válida. - Não definido;



3;Murilo;123456;agendapython.qroz@gmail.com;10/02/2015
1;Amora;123456;agendapython.qroz@outlook.com;26/08/2015
5;Nina;1234;agendapython.qroz@gmail.com;1234
4;Valentina;1234;agendapython.qroz@gmail.com;1234
6;Joca;1234;agendapython.qroz@gmail.com;27/01/1998
3;Luisa;1234;luisamsq66@yahoo.com;30/10/1966