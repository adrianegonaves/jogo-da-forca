import requests
import random

# A função `boas_vindas` é responsável por dar as boas vindas ao jogador.
def boas_vindas():
    print(f"\nQue a Força esteja com você, jovem Padawan!")


# A função `obter_nome_do_jogador` é responsável por pedir o nome do jogador e retornar.
def obter_nome_do_jogador():
    nome_do_jogador = input("Antes de começarmos, diga-nos: qual é o seu nome, jovem aprendiz Jedi? ")
    return nome_do_jogador


# A função `escolher_nivel` permite que o jogador escolha o nivel de dificuldade do jogo.
def escolher_nivel(nome_do_jogador):
    print(F"\nBem-vindo ao Jogo da Forca, {nome_do_jogador}! Que os céus da galáxia iluminem sua jornada.")
    print("\nEscolha seu destino na galáxia:")
    print("1. Caminho da Força (Fácil)")
    print("2. Lado Sombrio (Difícil)")
  
    # usando o while True temos um laço infinito até que o usuario insira um valor valido
    # o uso do bloco try except é para realizar o tratamento de erro, pois ele permite que você execute um bloco de código e, caso ocorra um erro, ocorre uma exceção e executa um código alternativo.
    while True:
        try:
            nivel = int(input("\nDigite o número do caminho que deseja seguir (1 ou 2): "))
            if nivel == 1:
                print(f"\nVocê escolheu o Caminho da Força. A luz guia você!")
                # retorna o nivel escolhido 1
                return nivel
            elif nivel == 2:
                print(f"\nVocê escolheu o Lado Sombrio. Apenas os mais fortes sobrevivem!")
                 # retorna o nivel escolhido 2
                return nivel
            else:
                print("Escolha inválida. Por favor, escolha entre 1 ou 2.")
        except Exception as error:
            print("Entrada inválida. Digite apenas o número 1 ou 2.")
            print(f"Ocorreu um erro: {error}")

# A função `busca_palavra_da_api` busca uma palavra aleatória na API Dicionario Aberto.
def busca_palavra_da_api():
    url = "https://api.dicionario-aberto.net/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("word", "").lower()
    except requests.RequestException as e:
        print("Erro ao buscar palavra da API:", e)
        return None
    

# A função `busca_palavra_no_arquivo` busca uma palavra aleatória no arquivo txt.
def busca_palavra_no_arquivo():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as arquivo:
            palavras = arquivo.read().split()
        return random.choice(palavras).lower()
    except FileNotFoundError:
        print("Erro: O arquivo 'palavras.txt' não foi encontrado.")
        return None
    

# A função `exibe_palavra_secreta` exibe a palavra secreta do jogo, substituindo as letras não adivinhadas por "_".
def exibe_palavra_secreta(palavra, letras_chutadas):
    # cria uma lista para armazenar a palavra que vai ser adivinhada com a letra ou com "_"
    palavra_secreta = []
    
    # percorre cada letra da palavra secreta
    for letra in palavra:
        # verifica se a letra está na palavra secreta, se tiver adiciona a letra, senão substitui por "_"
        if letra in letras_chutadas:
            palavra_secreta.append(letra)
        else:
            palavra_secreta.append('_')
    
    palavra_secreta_formata = " ".join(palavra_secreta)
    return palavra_secreta_formata

# A função `inicia_o_jogo` é responsavel pela logica geral do jogo.
# set são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.
def inicia_o_jogo(palavra, numero_de_tentativa):
    letras_chutadas = set()
    tentativa = numero_de_tentativa
    letra_da_palavra_secreta = set(palavra)

    print(f"\nQue a força esteja com você! Aqui está o desafio que lhe espera: \nVocê possui {tentativa} tentativas")
    print(exibe_palavra_secreta(palavra, letras_chutadas))

# enquanto as tentativas forem maior que 0 e não tiver adivinhado todas as letras continua o jogo
    while tentativa > 0 and letra_da_palavra_secreta != letras_chutadas:

        letra_para_adivinhar = input("\nQual será sua próxima jogada, jovem aprendiz Jedi? Digite uma letra: ").lower()

        if len(letra_para_adivinhar) != 1 or not letra_para_adivinhar.isalpha():
            print("Lembre-se, jovem Padawan, apenas uma letra por vez.")
            continue
        
        # verifica se a letra já tentou adivinhar a letra antes
        if letra_para_adivinhar in letras_chutadas:
            print("Essa letra já foi usada! Concentre-se e tente novamente.")

        # verifica se a letra está na palavra que está sendo adivinhada
        elif letra_para_adivinhar in letra_da_palavra_secreta:
            # caso a letra esteja na palavra secreta, adiciona no conjunto de letras já chutadas
            letras_chutadas.add(letra_para_adivinhar)
            print("Muito bem! Você acertou uma letra e está mais perto da vitória!")
        else:
            # caso contrario diminui 1 tentativa
            tentativa -= 1
            print(f"Errou! A letra '{letra_para_adivinhar}' não faz parte do destino. Restam {tentativa} tentativas.")

        print(exibe_palavra_secreta(palavra, letras_chutadas))

    # se as letra do conjunto de palavra secreta é igual ao conjunto de letras chutadas, acaba o jogo e o jogador vence
    if letra_da_palavra_secreta == letras_chutadas:
        print(f"\nParabéns, {palavra}! Você provou ser um verdadeiro Mestre Jedi!")
    else:
        # caso contrario o jogo acaba e o jogador perde
        print("\nInfelizmente, o Lado Sombrio venceu desta vez. A palavra era:", palavra)

# A função `main` que gerencia a aplicação.
def main():
    boas_vindas()
    nome_do_jogador = obter_nome_do_jogador()
    nivel = escolher_nivel(nome_do_jogador)

    if nivel == 1:
        palavra = busca_palavra_no_arquivo()
        numero_de_tentativa = 10
    else:
        palavra = busca_palavra_da_api()
        numero_de_tentativa = 5

    if palavra:
        inicia_o_jogo(palavra, numero_de_tentativa)
    else:
        print("Não foi possível obter uma palavra para o jogo.")

if __name__ == "__main__":
    main()
