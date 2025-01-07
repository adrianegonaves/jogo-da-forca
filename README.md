# Projeto de Fundamentos de Programação

Objetivo deste projeto é desenvolver um Jogo da Forca dinâmico em Python, no
âmbito da cadeira de Fundamentos de Programação, usando alguns conhecimentos
aprendidos em aula e também por meio de pesquisa extra classe.

## Identificação do aluno/grupo:

- Nome: Adriane Almeida Gonçalves nº 240000004

- Nome: Bruno Vasconcelos Hortelão nº 240001083

- Nome: Tomás António nº 240001360

## Criando o Jogo

1.**Desenvolvimento :**

Primeiro construimos um jogo simples, usando funções baiscas e que a interação fosse pelo terminal.

Ápos isso realizamos uma pesquisa para implementar a interface do jo, para ser mais visual e interativa.

2.**Estrutura:**

- logica - local que gerencia a "regra de negocio" do jogo
- interface - local que gerencia a interação da interface.
- main - local que gerencia toda a aplicação.

  3.**Interface:**

Para criar a interface usamos uma biblicoteca do Python chamada [Tkinter](https://docs.python.org/3/library/tkinter.html).

Tkinter é uma biblioteca que acompanha a instalação padrão do Python e permite desenvolver interfaces gráficas, dessa forma qualquer computador que tenha o interpretador Python instalado é capaz de criar interfaces gráficas usando o Tkinter.

#### Conceitos do Tkinter:

- Instanciamos a classe TK() através da variável root
- root.mainloop() : é o método que faz com que a janela fique sempre aberta, esperando algum evento(event)
- widget : se refe a um componente qualquer da interface gráfica ( botão, caixa de texto, entre outros)

  sintaxe para criar um widget : Nome_do_widget(mestre, configurações)

Usamos o Pack para trabalhar com geometria e posicionamento;

Estrutura basica de widgets

self.label_subtitulo = ttk.Label(
self.frame,
text="Que a Força esteja com você, jovem Padawan!",
font=("Helvetica", 12),
)
self.label_subtitulo.pack(pady=10)

Vamos ver algumas configurações de estilo mais comuns que podemos definir:

Width – Largura do widget;
Height – Altura do widget;
Text – Texto a ser exibido no widget;
Font – Família da fonte do texto;
Fg – Cor do texto do widget;
Bg – Cor de fundo do widget;
Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).
Para receber dados do usuário vamos usar o widget Entry, onde os mesmos são capturados como string, de forma semelhante ao método input

Aquivo main.py.

## Referência

- [DevMedia](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/styleguide/)
- [Introdução a Python](https://www.cos.ufrj.br/~bfgoldstein/python/tutorialtkinter.pdf)
