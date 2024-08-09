from time import sleep #Importando somente a função Sleep da biblioteca Time
print('Bem vindo(a) a Livraria da Millenna Mazaro')
print('-' * 50)
print('-' * 17, 'MENU PRINCIPAL', '-' * 17)

biblioteca = [] #Inicializando Lista vazia
id_livro = 1 #Inicializando o contador de ID

def cadastrar_livro(): #função para cadastrar livros
    global id_livro
    print('-' * 50)
    print('-' * 14, 'MENU CADASTRAR LIVRO', '-' * 14)
    print(f'ID do livro: {id_livro}') #Exibe o ID do livro
    nome_livro = input('Por favor entre com o nome do livro:\n')
    autor_livro = input('Por favor entre com o autor do livro:\n')
    editora_livro = input('Por favor entre com a editora do livro:\n')
    biblioteca.append({'id': id_livro, 'nome': nome_livro, 'autor': autor_livro, 'editora': editora_livro})
    id_livro += 1 #Incrementa o ID para o próximo livro
    print('Cadastrando...')
    sleep(2)
    print('Cadastrado com sucesso!')
    print('-' * 50)

def consultar_livro(): #função para consultar livros
    while True:
        print('-' * 50)
        print('-' * 14, 'MENU CONSULTAR LIVRO', '-' * 14)
        consulta_opcao = int(input(''' Escolha a opção desejada: 
        1 - Consultar Todos os Livros
        2 - Consultar Livro por ID
        3 - Consultar Livro por Autor
        4 - Retornar ao Menu Principal
        >> '''))

        if consulta_opcao == 1: # Todos os Livros
            print('-' * 50)
            print('Livros cadastrados:')
            for livro in biblioteca:
                print(f'ID: {livro["id"]}\nNome: {livro["nome"]}\nAutor: {livro["autor"]}\nEditora: {livro["editora"]}\n')
            if not biblioteca:
                print('Nenhum Livro Cadastrado.')

        elif consulta_opcao == 2: # Livros por ID
            if biblioteca:
                id_consulta = int(input('Digite o ID do livro que deseja consultar:\n'))
                encontrado = False
                for livro in biblioteca:
                    if livro["id"] == id_consulta:
                        print(f'ID: {livro["id"]}\nNome: {livro["nome"]}\nAutor: {livro["autor"]}\nEditora: {livro["editora"]}\n')
                        encontrado = True
                        break
                if not encontrado:
                    print('Livro com ID não encontrado.')
            else:
                print('Nenhum livro cadastrado.')

        elif consulta_opcao == 3: # Livros por Autor
            if biblioteca:
                autor_consulta = input('Digite o autor do livro que deseja consultar:\n')
                encontrados = [livro for livro in biblioteca if livro["autor"].lower() == autor_consulta.lower()]
                if encontrados:
                    for livro in encontrados:
                        print(f'ID: {livro["id"]}, Nome: {livro["nome"]}, Autor: {livro["autor"]}, Editora: {livro["editora"]}')
                else:
                    print('Nenhum livro encontrado para esse autor.')
            else:
                print('Nenhum livro cadastrado.')

        elif consulta_opcao == 4:
            break  # Retornar ao menu principal

        else:
            print('Opção inválida. Tente novamente.')

def remover_livro(): #função para remover livro da lista
    print('-' * 50)
    id_remover = int(input('Digite o ID do livro que deseja remover:\n'))
    encontrado = False
    for livro in biblioteca:
        if livro["id"] == id_remover: #Verifica se o ID do livro corresponde ao ID fornecido
            biblioteca.remove(livro)
            print('Livro removido com sucesso.')
            encontrado = True
            break
    if not encontrado:
        print('ID não encontrado.')

while True: #looping menu principal
    print('-' * 50)
    print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
    opcao = int(input(''' Escolha a opção desejada: 
    1 - Cadastrar Livro
    2 - Consultar Livro(s)
    3 - Remover Livro
    4 - Sair
    >> '''))

    if opcao not in [1, 2, 3, 4]:
        print('Opção inválida. Tente novamente.')

    elif opcao == 4: #Finaliza o Programa
        print('Finalizando...')
        sleep(2)
        print('Fim do programa.')
        break

    elif opcao == 1:
        cadastrar_livro()

    elif opcao == 2:
        consultar_livro()

    elif opcao == 3:
        remover_livro()
