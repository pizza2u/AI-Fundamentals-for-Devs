'''Descrição
Imagine que você foi designado a criar um algoritmo para analisar o sentimento de um comentário fornecido pelo usuário, simulando analises de sentimentos, um assunto muito comentado dentro do Machine Learning. O programa solicitará ao usuário que insira um comentário, e em seguida, dividirá esse comentário em palavras individuais.

Após isso, ele contará o número de palavras positivas, negativas e neutras dentro do comentário, baseando-se em uma lista pré-definida de palavras-chave. As palavras consideradas positivas incluem "bom", "ótimo", "excelente", "maravilhoso", "gostei" e "incrível" enquanto as palavras negativas incluem "ruim", "péssimo", "horrível", "terrível" e "odeio". Já as palavras neutras incluem "mas", "deixou", "apesar" e "embora"

Depois de calcular as contagens de palavras positivas e negativas, o programa determinará o sentimento predominante do comentário. Se houver mais palavras positivas do que negativas, o sentimento será considerado positivo. Se houver mais palavras negativas do que positivas, o sentimento será considerado negativo. Caso contrário, se houver um número igual de palavras positivas e negativas, o sentimento será neutro.

Entrada
O usuário será solicitado a fornecer um comentário como entrada para o programa.

Saída
O programa exibirá o sentimento do comentário inserido pelo usuário, que pode ser "Positivo", "Negativo" ou "Neutro", dependendo da análise das palavras-chave no comentário.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
A mentoria foi incrível, aprendi muito!	Sentimento: Positivo
O clima hoje está terrível, odeio dias quentes.	Sentimento: Negativo
A comida estava boa, mas o serviço deixou a desejar.	Sentimento: Neutro
Atenção
'''

import re

def analyze_sentiment():
    comentario = input()
    palavras = re.findall(r'\b\w+\b', comentario.lower())

    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    # Verifica se há mais palavras positivas do que negativas no comentário e se não há palavras neutras. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    # Verifica se há mais palavras negativas do que positivas no comentário e se não há palavras neutras. Se essa condição for verdadeira, o comentário é considerado negativo.
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    # Se o número de palavras positivas for igual ao número de palavras negativas e não houver palavras neutras, o comentário é considerado neutro.
    elif count_positivo == count_negativo and count_neutro == 0:
        return "Neutro"
    # Caso contrário, o comentário é considerado misto.
    else:
        return "Neutro"

sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
