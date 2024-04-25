'''
Descrição
Neste desafio, você será solicitado a criar um algoritmo que avalia se um prompt fornecido pelo usuário está adequado. O programa solicitará ao usuário que insira um prompt e, em seguida, verificará se o prompt contém palavras-chave relevantes. As palavras-chave consideradas relevantes serão "inteligência artificial", "sistemas de recomendação online", "exemplo de conversação", "explique conceitos" e "dicas de tecnologia". Se o prompt incluir pelo menos uma dessas palavras-chave, o programa informará que o prompt está adequado; caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

Entrada
O usuário será solicitado a inserir um prompt como entrada para o programa.

Saída
O programa exibirá feedback para o usuário com base na avaliação do prompt inserido. Se o prompt contiver palavras-chave relevantes, o programa informará que o prompt está adequado. Caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Por favor, explique conceitos de inteligência artificial.	O prompt está adequado.
Crie exemplos de conversação.	O prompt está adequado.
Qual é a coisa mais bonita do mundo?	O prompt não está adequado. Inclua palavras-chave relevantes.

'''

def avaliar_prompt(prompt):
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia"]

    for palavra in palavras_chave:
        if palavra in prompt:
            return "O prompt está adequado."

    return "O prompt não está adequado. Inclua palavras-chave relevantes."

prompt_usuario = input("Digite o prompt: ")

feedback_usuario = avaliar_prompt(prompt_usuario)

print(feedback_usuario)
