import re


def nocoes_basicas():
    print("\nNoções Básicas")
    string = 'Testando expressões regulares em Python'
    print(re.findall(r'regulares', string))  # Função que retorna todas as ocorrências de 'teste' dentro da string
    print(re.sub(r'regulares', 'ABC', string))  # Função que substitui 'regulares' por 'ABC' dentro da string
    print(re.search(r'regulares', string))  # Função que retorna instancia de Match se
    # capturar alguma palavra válida, ou None se não achar

    regex = re.compile(r'teste')  # O Python precisa sempre compilar uma nova expressão regular,
    # mas ao usar compile, ele compila ela e depois não precisa compilar de novo


def meta_caracteres():
    # \ - Usada para escapar caracteres reservados
    # | - Ou
    # . - Qualquer caractere (com exceção de quebra de linha)
    # [] - Dentro dos colchetes são colocados caracteres, é aceito pela regex qualquer caractere dentro dos colchetes
    # ^ - Indica o início da string
    # $ - Indica o fim da string
    frase = 'Python python'

    print("\nMeta Caracteres")
    print(re.findall(r'Python|python', frase))  # Aceita 'Python' ou 'python'
    print(re.findall(r'..thon', frase))  # Aceita qualquer palavra com 'thon' sucedido de dois caracteres qualquer
    print(re.findall(r'[Pp]ython', frase))  # Aceita palavras que comecem com 'P' ou 'p' e terminam com 'ython'
    print(re.findall(r'^[Pp]ython', frase))  # Aceita 'Python' ou 'python' se estiver no começo da string
    print(re.findall(r'[Pp]ython$', frase))  # Aceita 'Python' ou 'python' se estiver no fim da string


def quantificadores():
    # Quantificadores: Ditam quantas vezes tal cadeia de caracteres deve aparecer
    # * - 0 ou n
    # + - 1 ou n
    # ? - 0 ou 1
    # {} - Qualquer range desejado
    frase = 'goooooooooool gl'

    print("\nQuantificadores")
    print(re.findall(r'go*l', frase))  # Palavras que começam com g, terminam com l e tem 0 ou n 'o' entre 'g' e 'l'
    print(re.findall(r'go+l', frase))  # Palavras que tem 1 ou n 'o' entre 'g' e 'l'
    print(re.findall(r'go?l', frase))  # Palavras que tem 0 ou 1 'o' entre 'g' 'l'
    print(re.findall(r'go{6,12}l', frase))  # Palavras que tem de 6 a 12 'o' entre 'g' e 'l'

    # * e + são quantificadores gulosos, então eles vão consumindo caracteres sem parar
    # Colocando um '?' após eles, os torna não gulosos
    frase = 'Python v2? Python v3? Python v3.8?'

    print("\nQuantificadores Gulosos")
    print(re.findall(r'Python.*\?', frase))  # Guloso
    print(re.findall(r'Python.*?\?', frase))  # Não guloso


def grupos():
    # Grupos são uma estrutura formada por (), ao usar um grupo, é salvada a expressão regular dentro dele
    # Possibilita reutilização da regex para encurtar a expressão, ou até para substituir texto
    # Os grupos podem ser acessados através de sua posição na regex, usando '\x', onde x é a posição do grupo na regex
    # O número da posição é obtido através da contagem de parênteses abertos '('
    # Para a regex não salvar o grupo, usa-se '?:' no início do grupo
    html = '<p>Paragrafo</p> <section>Python</section> <div> </div>'

    print("\nGrupos")
    print(html)
    print(re.sub(r'(<(.+?)>)(.+?)(</\2>)', r'\1Isto aqui é um elemento \2\4', html))  # Substituindo texto usando grupos


def sequencias_especiais():
    # Sequencias especiais são representados por \ seguido da letra que representa a sequencia
    # \w todas os caracteres (não considera barra de espaço ou quebra de linha)
    # \d todas os dígitos
    # \s todas os tipos espaços em branco, incluindo quebra de linha
    # \b representa a borda inicial ou final de uma cadeia de caracteres
    # Se a letra for maiúscula significa a negação da sequencia da letra minúscula
    frase = 'A proclamação da república aconteceu no dia 15 de novembro de 1889.'

    print("\nSequencias Especiais")
    print(re.findall(r'\w+', frase))  # Todas as palavras
    print(re.findall(r'\d+', frase))  # Todos os números
    print(re.findall(r'\w*?[Aa]\b', frase))  # Todas as palavras terminadas em a


def flags():
    # Flags são usadas para validar certos caracteres ou palavras no texto passado por completo
    # re.IGNORECASE - Não difere letras maiúsculas de minúsculas
    # re.ASCII - Considera somente caracteres no padrão ASCII
    # re.MULTILINE - Considera cada linha do texto passado como um novo texto
    # re.DOTALL - Considera agora quebras de linha
    emails = '''
    Joao@gmail.com online
    Marcos@gmail.com offline
    Ana@gmail.com online
    '''

    print("\nFlags")
    print(re.findall(r'\w+?@gmail.com\s(?:ONLINE|offline)$', emails, flags=re.MULTILINE | re.IGNORECASE))
    print(re.findall(r'\w+', emails, flags=re.ASCII))


def capturando_condicionalmente():
    # Capturando palavras condicionadas a outras palavras
    # Usando grupos, colocar ?= antes da palavra que atua como condição de captura para capturar
    # palavras que contém o grupo com o ?=
    # Para capturar palavras que não contém tal palavra, usa-se ?! ao invés de ?=
    emails = '''
    Joao@gmail.com online
    Marcos@gmail.com offline
    Ana@gmail.com online
    '''
    print("\nCapturando palavras condicionalmente")
    print(re.findall(r'(\w+?@gmail.com)\s(?=online)', emails))  # Usuários online
    print(re.findall(r'(\w+?@gmail.com)\s(?=offline)', emails))  # Usuários offline


def tutorial_basico():
    nocoes_basicas()
    meta_caracteres()
    quantificadores()
    grupos()
    sequencias_especiais()
    flags()
    capturando_condicionalmente()


# Funções que validam campos
def valida_email():
    option = 1
    while option == 1:
        email = input('Validando email, digite algum: ')
        email_regex = re.compile(r'^\w+(?:[.\-+!&%]\w+)*@\w+(?:[.\-]\w+)+$')
        # No email, apenas alguns caracteres especiais podem existir
        match = email_regex.search(email)
        print('Válido' if match else 'Não válido')
        option = int(input('Quer tentar de novo? Digite 1 para mais uma vez: '))


def valida_ip():
    option = 1
    while option == 1:
        ip = input('Validando IP, digite algum: ')
        ip_regex = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|'
                              r'1[0-9]{2}|[1-9][0-9]|[0-9])$', flags=re.M)
        match = ip_regex.search(ip)
        print('Válido' if match else 'Não válido')
        option = int(input('Quer tentar de novo? Digite 1 para mais uma vez: '))


def valida_cpf():
    # Não validando CPFs sequenciais, como 000.000.000-00
    option = 1
    while option == 1:
        cpf = input('Validando cpf, digite algum (digite da forma xxx.xxx.xxx-xx): ')
        cpf_regex = re.compile(r'^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$', flags=re.M)
        match = cpf_regex.search(cpf)
        print('Válido' if match else 'Não válido')
        option = int(input('Quer tentar de novo? Digite 1 para mais uma vez: '))


def valida_senha():
    option = 1
    while option == 1:
        senha = input('Validando senhas fortes(ao menos 10 caracteres, 1 dígito e uma maiuscula), digite alguma: ')
        senha_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{10,}$', flags=re.M)
        match = senha_regex.search(senha)
        print('Válido' if match else 'Não válido')
        option = int(input('Quer tentar de novo, digite 1 para mais uma vez: '))


def valida_telefone():
    option = 1
    while option == 1:
        telefone = input('Validando telefones celulares brasileiros (padrão +55 xx 9xxxxxxxx), digite algum: ')
        telefone_regex = re.compile(r'^\+55 \d{2} 9\d{8}$')
        match = telefone_regex.search(telefone)
        print('Válido' if match else 'Não válido')
        option = int(input('Quer tentar de novo? Digite 1 para mais uma vez: '))


def valida_notacao_cientifica():
    option = 1
    while option == 1:
        notacao = input('Validando números em notação científica, positivos ou negativos,'
                        ' da forma n,n*10^n, ex: 1,2*10^3 digite algum: ')
        notacao_regex = re.compile(r'^[+-]?[1-9],\d+?\*10\^[-]?\d+?$')
        match = notacao_regex.search(notacao)
        print('Válido' if match else 'Não válido')
        option = int(input('Quer tentar de novo? Digite 1 para mais uma vez: '))


def menu_validacao():
    num = 3
    while num != 0:
        num = int(input('\nMenu de Validação de Campos\n'
                        'Digite 1 para validar email\nDigite 2 para validar IP\nDigite 3 para validar CPF\n'
                        'Digite 4 para validar senha\nDigite 5 para validar telefone\n'
                        'Digite 6 para validar números em notação científica\nDigite 0 para sair\n'))
        if num == 1:
            valida_email()
        elif num == 2:
            valida_ip()
        elif num == 3:
            valida_cpf()
        elif num == 4:
            valida_senha()
        elif num == 5:
            valida_telefone()
        elif num == 6:
            valida_notacao_cientifica()
        elif num == 0:
            pass
        else:
            print('Essa opção não existe')


if __name__ == '__main__':
    selecao = 10
    while selecao != 0:
        selecao = int(input('\nDigite 1 para ir ao tutorial básico\nDigite 2 para ir ao menu de validação de campos\n'
                            'Digite 0 para sair\n'))
        if selecao == 1:
            tutorial_basico()
        elif selecao == 2:
            menu_validacao()
        elif selecao == 0:
            break
        else:
            print('Opção inválida')
