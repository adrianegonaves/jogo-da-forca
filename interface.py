import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, DARK, INFO, DANGER
from tkinter import messagebox

class JogoDaForcaInterface:
    def __init__(self, janela, logica):
        self.janela = janela
        self.logica = logica

        # configurações da tela, como título e tamanho
        self.janela.title("Fundamentos de Programação - Jogo da Forca")
        self.janela.geometry("800x400")
        
        # container pai/janela principal
        self.frame = ttk.Frame(janela)
        self.frame.pack(pady=30)


        self.exibir_tela_inicial()

    def exibir_tela_inicial(self):

        self.limpar_tela()

        self.label_titulo = ttk.Label(
            self.frame, text="Fundamentos de Programação - Jogo da Forca", font=("Arial", 18, "bold")
        )
        self.label_titulo.pack()


        self.label_subtitulo = ttk.Label(
            self.frame,
            text="Que a Força esteja com você, jovem Padawan!",
            font=("Arial", 12),
        )
        self.label_subtitulo.pack(pady=10)

        self.label_nome = ttk.Label(
            self.frame, 
            text="Diga o seu nome, jovem aprendiz Jedi?",
            font = ("Arial", 12)
        )
        self.label_nome.pack()

        # o entry é o input
        self.entry_nome = ttk.Entry(
            self.frame,
            font = ("Arial", 12),
            width=20,
            bootstyle=DARK
        )
        self.entry_nome.pack(pady=5)

        self.button_iniciar = ttk.Button(
            self.frame, 
            text="Jogar", 
            command=self.iniciar_jogo,
            width=30,
            bootstyle=SUCCESS,

        )
        self.button_iniciar.pack(pady=10)

    def iniciar_jogo(self):
        # o metodo get retorna o texto atual da entrada como uma string.
        nome_do_jogador = self.entry_nome.get().strip()
        # se não existir o nome do jogador retorna uma caixa de texto com um alerta
        if not nome_do_jogador:
            messagebox.showwarning("Atenção", "Por favor, digite seu nome, jovem aprendiz Jedi!")
            return

        # função nome do jogador recebe o nome do jogador
        self.logica.definir_nome_jogador(nome_do_jogador)
        self.escolher_nivel_do_jogo()

    def escolher_nivel_do_jogo(self):
        self.limpar_tela()

        self.label_subtitulo = ttk.Label(
            self.frame,
            text=f"Bem-vindo ao Jogo da Forca, {self.logica.jogador}.",
            font=("Helvetica", 12),
        )
        self.label_subtitulo.pack(pady=10)

        self.label_mensagem= ttk.Label(
            self.frame,
            text=f"Que os céus da galáxia iluminem sua jornada!",
            font=("Helvetica", 12),
        )
        self.label_mensagem.pack(pady=10)

        self.label_dificuldade = ttk.Label(
            self.frame, text="Escolha seu destino na galáxia:"
        )
        self.label_dificuldade.pack()

        self.button_facil = ttk.Button(
            self.frame,
            text="Caminho da Força (Fácil)",
            command=lambda: self.jogo(1),
            width=30,
            bootstyle=INFO
        )
        self.button_facil.pack(pady=5)

        self.button_dificil = ttk.Button(
            self.frame,
            text="Lado Sombrio (Difícil)",
            command=lambda: self.jogo(2),
            width=30,
            bootstyle=INFO
        )
        self.button_dificil.pack(pady=5)

    def jogo(self, dificuldade):
        self.logica.iniciar_jogo(dificuldade)
        self.jogar()

    def jogar(self):
        self.limpar_tela()

        self.label_tentativas = ttk.Label(self.frame, text=f"Que a força esteja com você! Aqui está o desafio que lhe espera: Você possui {self.logica.tentativas} tentativas")
        self.label_tentativas.pack()

        self.label_letras_chutadas = ttk.Label(
        self.frame,
        text="Letras já tentadas: Nenhuma",
        font=("Helvetica", 10)
        )
        self.label_letras_chutadas.pack(pady=5)

        self.label_chute = ttk.Label(self.frame, text="Digite uma letra: ")
        self.label_chute.pack()

        self.entry_chute = ttk.Entry(
            self.frame,
            width=20,
            bootstyle=DARK
        )
        self.entry_chute.pack()

        self.label_palavra = ttk.Label(
            self.frame, text=self.logica.exibe_palavra_secreta(), font=("Helvetica", 14)
        )
        self.label_palavra.pack(pady=10)

        self.button_enviar = ttk.Button(
            self.frame, 
            text="Enviar",
            width=30,
            command=self.tentar_letra,
            bootstyle=SUCCESS
        )
        self.button_enviar.pack(pady=10)

        self.label_feedback = ttk.Label(self.frame, text="", font=("Helvetica", 10))
        self.label_feedback.pack(pady=10)

    def tentar_letra(self):
        letra = self.entry_chute.get().strip().lower()
        self.entry_chute.delete(0, ttk.END)

        if len(letra) != 1 or not letra.isalpha():
            self.label_feedback.config(
                text="Digite apenas uma letra válida!", foreground="red"
            )
            return

        resultado = self.logica.tentar_letra(letra)
        self.label_palavra.config(text=self.logica.exibe_palavra_secreta())

         # Atualize o rótulo de letras chutadas
        letras_chutadas = ", ".join(sorted(self.logica.letras_chutadas))
        self.label_letras_chutadas.config(
            text=f"Letras já tentadas: {letras_chutadas}"
        )

        # Atualize o rótulo de tentativas restantes
        self.label_tentativas.config(
            text=f"Você possui {self.logica.tentativas} tentativas restantes."
        )

        if resultado == "acertou":
            self.label_feedback.config(
                text="Muito bem! Você acertou uma letra!", foreground="green"
            )
        elif resultado == "errou":
            self.label_feedback.config(
                text=f"Errou! Restam {self.logica.tentativas} tentativas.", foreground="red"
            )
        elif resultado == "repetida":
            self.label_feedback.config(
                text="Essa letra já foi usada! Tente novamente.",foreground="orange"
            )

        if self.logica.jogo_acabou():
            self.finalizar_jogo()

    def finalizar_jogo(self):

        self.limpar_tela()

        if self.logica.vitoria():
            messagebox.showinfo(
                "Parabéns!",
                f"Você provou ser um verdadeiro Mestre Jedi! A palavra era: {self.logica.palavra}",
            )
        else:
            messagebox.showinfo(
                "Game Over",
                f"Infelizmente, o Lado Sombrio venceu desta vez. A palavra era: {self.logica.palavra}",
            )
        self.exibir_botao_recomecar()

    def exibir_botao_recomecar(self):
        self.limpar_tela()

        self.label_final = ttk.Label(
            self.frame, text="Deseja jogar novamente?", font=("Helvetica", 14)
        )
        self.label_final.pack(pady=10)

        self.button_recomecar = ttk.Button(
            self.frame, text="Recomeçar",
            command=self.exibir_tela_inicial,
            width=30,
            bootstyle=SUCCESS
        )
        self.button_recomecar.pack(pady=10)

        self.button_sair = ttk.Button(
            self.frame, text="Sair", 
            command=self.master.quit,
            width=30,
            bootstyle=DANGER
        )
        self.button_sair.pack(pady=10)

    def limpar_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
