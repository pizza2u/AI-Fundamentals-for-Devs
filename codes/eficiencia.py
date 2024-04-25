'''
Desafio
Neste desafio, você será solicitado a fornecer uma breve descrição de boas práticas de refatoração de código em três áreas específicas: identificação clara de funções, separação da entrada de dados e uso de nomes descritivos para variáveis e funções.Cada descrição deve indicar como o código pode ser melhorado nesses aspectos. O objetivo é simularmos a ação de pesquisas em IAs Generativas de busca e pesquisa, dessa forma, cada entrada simula um bom prompt de pesquisa.

Entrada:
A entrada será uma string de texto que representa um bom promtp de pesquisa para IAs Generativas.Após inserir sua descrição, o programa irá processá-la e fornecer um retorno sobre a prática de refatoração sugerida. Se a entrada corresponder a uma das três áreas especificadas, o programa irá sugerir a respectiva melhoria. Caso contrário, informará que a opção é inválida.

Saída:
Após inserir sua descrição, o programa irá processá-la e fornecer um retorno sobre a prática de refatoração sugerida. Se a entrada corresponder a uma das três áreas especificadas, o programa irá sugerir a respectiva melhoria. Caso contrário, informará que a opção inválida.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Dica de boas práticas de refatoração de código, nas funções.	Separe funções em unidades coesas e com responsabilidades únicas.
Dica de boas práticas de refatoração de código, nas entrada de dados.
Valide e normalize as entradas para evitar inconsistências.
Dica de boas práticas de refatoração de código, nomenclaturas.	Use nomes descritivos para variáveis e funções.

'''

def identificar_funcoes(texto):
    # Mensagem sobre a identificação clara de funções
    return "Separe funções em unidades coesas e com responsabilidades únicas."

def entrada_de_dados(texto):
    # Mensagem sobre separação da entrada de dados
    return "Valide e normalize as entradas para evitar inconsistências."

def nomenclatura_significativa(texto):
    # Mensagem sobre uso de nomes descritivos
    return "Use nomes descritivos para variáveis e funções."

def processar_entrada(texto):
    # Dicionário mapeando textos para funções
    opcoes = {
        "Dica de boas práticas de refatoração de código, nas funções.": identificar_funcoes,
        "Dica de boas práticas de refatoração de código, nas entrada de dados.": entrada_de_dados,
        "Dica de boas práticas de refatoração de código, nomenclaturas.": nomenclatura_significativa
    }

    # Verifica se o texto está presente nas opções
    if texto in opcoes:
        return opcoes[texto](texto)
    else:
        return "Opção inválida."

def desafio():
    entrada = input()
    saida = processar_entrada(entrada)
    print(saida)

desafio()
