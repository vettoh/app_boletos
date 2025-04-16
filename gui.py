
from tkinter import ttk
import tkinter as Tk
from database import inserir_boleto


def enviar_dados(valor_nome,valor_data_de_pedido,valor_da_compra,valor_parcelas,valor_vencimento):
    inserir_boleto(valor_nome,valor_data_de_pedido,valor_da_compra,valor_parcelas,valor_vencimento)

def confirmacao():
    valor_nome = nome.get()
    valor_data_de_pedido = data_compra.get() 
    valor_da_compra = valor.get()
    valor_parcelas = parcelas.get()
    valor_vencimento = vencimento.get()

    FRM.destroy()
    # como destruimos tudo o que havia no primeiro FRM tivemos que cirar um novo, para a exibição da nova página
    FRM2 = ttk.Frame(janela, padding=10)
    FRM2.grid()
    
    LABEL_TITULO = Tk.Label(FRM2,text="CONFIRME SE OS DADOS ESTÃO CERTOS")
    LABEL_TITULO.grid(column=4,row=1)

    nome_FRM2 = Tk.Label(FRM2, text= f'{valor_nome}')
    nome_FRM2.grid(column=1, row=6)

    data_de_pedido_FRM2 = Tk.Label(FRM2, text= f'{valor_data_de_pedido}')
    data_de_pedido_FRM2.grid(column=2, row=6)

    valor_da_compra_FRM2 = Tk.Label(FRM2, text= f'{valor_da_compra}')
    valor_da_compra_FRM2.grid(column=3, row=6)

    parcelas_FRM2 = Tk.Label(FRM2, text= f'{valor_parcelas}')
    parcelas_FRM2.grid(column=4, row=6)

    vencimento_FRM2 = Tk.Label(FRM2, text= f'{valor_vencimento}')
    vencimento_FRM2.grid(column=5, row=6)

   #temos que usar lambda aqui, pq para adicionar o valor dos entrys aqui da forma convencional, seria executada a função na hora de criar o botão e isso resultaria em um erro, lambda cria uma função anônima, que será executa somente ao clicar o botão
    botao_confirmar = Tk.Button(FRM2, text="CONFIRMAR", command=lambda:enviar_dados(valor_nome,valor_data_de_pedido,valor_da_compra,valor_parcelas,valor_vencimento))
    botao_confirmar.grid(column=4, row=8)    







janela = Tk.Tk()
largura = 650
altura = 400
janela.geometry(f"{largura}x{altura}")

FRM = ttk.Frame(janela, padding=10)
FRM.grid()

#labels tabela
TITULO = Tk.Label(FRM, text="ALERTA DE BOLETOS")
TITULO.grid(column=4, row=1)

NOME = Tk.Label(FRM, text="NOME")
NOME.grid(column=1, row=3)

DATA_COMPRA = Tk.Label(FRM, text="DATA DA COMPRA")
DATA_COMPRA.grid(column=3, row=3)

VALOR = Tk.Label(FRM, text="VALOR")
VALOR.grid(column=4, row=3)

PARCELAS = Tk.Label(FRM, text="PARCELAS")
PARCELAS.grid(column=6, row=3)

DATA_VENCIMENTO = Tk.Label(FRM, text="VENCIMENTO")
DATA_VENCIMENTO.grid(column=5, row=3)

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

cadastrar = Tk.Button(FRM, text="CADASTRAR", command=confirmacao)
cadastrar.grid(column=4, row=(5))

botao_historico_boletos = Tk.Button(janela, text= "BOLETOS CADASTRADOS")
botao_historico_boletos.place(x=250,y=180)


janela.mainloop()

