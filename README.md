Fundamentos de programação

Jogo da Forca.

Objetivo do jogo

Criação do Jogo

A estrutura do codigo foi dividida em tres partes:

logica - local que gerencia a "regra de negocio" do jogo
interface - local que gerencia a interação da interface.
main - local que gerencia toda a aplicação.

Interface

Para criar a interface usamos uma biblicoteca do Python chamada [Tkinter](https://docs.python.org/3/library/tkinter.html)
Tkinter é uma biblioteca que acompanha a instalação padrão e permite desenvolver interfaces gráficas, dessa forma qualquer computador que tenha o interpretador Python instalado é capaz de criar interfaces gráficas usando o Tkinter.

Conceitos do Tkinter:
instanciamos a classe TK() através da variável root, que foi criada no final do código. Essa classe permite que os widgets possam ser utilizados na aplicação
método root.mainloop() para exibirmos a tela

O módulo Tkinter oferece três formas de trabalharmos com geometria e posicionamento:

Pack;
Grid;
Place

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

Referencias usadas :
[DevMedia](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
