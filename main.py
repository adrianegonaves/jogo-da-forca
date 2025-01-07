from logica import JogoDaForcaLogica
from  interface import JogoDaForcaInterface
import tkinter as tk


def main():
    root = tk.Tk()
    logic = JogoDaForcaLogica()
    application = JogoDaForcaInterface(root, logic)
    root.mainloop()


if __name__ == "__main__":
    main()
