import random
import requests


class JogoDaForcaLogica:
    def __init__(self):
        self.jogador = ""
        self.palavra = ""
        self.tentativas = 0
        self.letras_chutadas = set()
        self.letras_palavra = set()

    def definir_nome_jogador(self, nome):
        self.jogador = nome.capitalize()

    def pegar_palavra_api(self):
        url = "https://api.dicionario-aberto.net/random"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("word", "").lower()
        except requests.RequestException:
            return None

    def pegar_palavra_arquivo(self):
        try:
            with open("palavras.txt", "r", encoding="utf-8") as file:
                palavras = file.read().split()
            return random.choice(palavras).lower()
        except FileNotFoundError:
            return None

    def iniciar_jogo(self, dificuldade):
        if dificuldade == 1:
            self.palavra = self.pegar_palavra_arquivo()
            self.tentativas = 10
        else:
            self.palavra = self.pegar_palavra_api()
            self.tentativas = 5

        if not self.palavra:
            self.palavra = "forca"

        self.letras_palavra = set(self.palavra)
        self.letras_chutadas.clear()

    def exibe_palavra_secreta(self):
        palavra_secreta = []
        # percorre cada letra da palavra secreta
        for letra in self.palavra:
            # verifica se a letra está na palavra secreta, se tiver adiciona a letra, senão substitui por "_"
            if letra in self.letras_chutadas:
                palavra_secreta.append(letra)
            else:
                palavra_secreta.append('_')
        
            palavra_secreta_formata = " ".join(palavra_secreta).capitalize()
        return palavra_secreta_formata

    def tentar_letra(self, letra):
        if letra in self.letras_chutadas:
            return "repetida"

        self.letras_chutadas.add(letra)

        if letra in self.letras_palavra:
            return "acertou"
        else:
            self.tentativas -= 1
            return "errou"

    def jogo_acabou(self):
        palavra_descoberta = all(letra in self.letras_chutadas for letra in self.palavra)
        return palavra_descoberta or self.tentativas <= 0

    def vitoria(self):
       return all(letra in self.letras_chutadas for letra in self.palavra)
