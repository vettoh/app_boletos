from tkinter import *
from tkinter import ttk
import tkinter as Tk

janela = Tk.Tk()
largura = 800
altura = 400
janela.geometry(f"{largura}x{altura}")

FRM = ttk.Frame(janela, padding=10)
FRM.grid()

#labels tabela
TITULO = Tk.Label(FRM, text="ALERTA DE BOLETOS").grid(column=4, row=1)
NOME = Tk.Label(FRM, text="NOME").grid(column=1, row=3)
DATA_COMPRA = Tk.Label(FRM, text="DATA DA COMPRA").grid(column=3, row=3)
VALOR = Tk.Label(FRM, text="VALOR").grid(column=4, row=3)
PARCELAS = Tk.Label(FRM, text="PARCELAS").grid(column=6, row=3)
DATA_VENCIMENTO = Tk.Label(FRM, text="VENCIMENTO").grid(column=5, row=3)

#entrys
nome = Tk.Entry(FRM)
nome.grid(column=1, row=4)

data_compra = Tk.Entry(FRM)
data_compra.grid(column=3, row=4)

valor = Tk.Entry(FRM)
valor.grid(column=4, row=4)

parcelas = Tk.Entry(FRM)
parcelas.grid(column=5, row=4)

vencimento = Tk.Entry(FRM)
vencimento.grid(column=6, row=4)

janela.mainloop()

