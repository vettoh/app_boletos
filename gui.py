
from tkinter import ttk
import tkinter as Tk
from database import inserir_boleto, ver_boletos
from main import enviar_email
from datetime import datetime
from utils import formatar_data_vencimento
from scheduler import checar_e_enviar_boletos


def voltar():
    FRM2.grid_forget()
    FRM.grid()
   

def visualizacao_tabela():
    toplevel_tabela = Tk.Toplevel(janela)
    toplevel_tabela.title = "BOLETOS CADASTRADOS"
    toplevel_tabela.geometry = ("400x400")
    
    colunas = ("id", "nome","data do pedido", "valor", "parcelas", "vencimento")
    tree = ttk.Treeview(toplevel_tabela,columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    #adicionar dados vindo do banco
    boletos = ver_boletos()
    
    for boleto in boletos:
        tree.insert("","end", values=boleto)
    tree.pack(fill="both", expand=True)

def enviar_dados(empresa,data_compra, valor, parcelas, vencimento_str):
    vencimento_formatado = formatar_data_vencimento(vencimento_str)
    if not vencimento_formatado:
        print("data de vencimento inválida")
        return
    inserir_boleto(empresa, data_compra, valor, parcelas, vencimento_formatado)
    print("boleto inserido com sucesso")    

def confirmacao():
    valor_nome = nome.get()
    valor_data_de_pedido = data_compra.get() 
    valor_da_compra = valor.get()
    valor_parcelas = parcelas.get()
    valor_vencimento = vencimento.get()

    try:
        valor_vencimento_br = datetime.strptime(valor_vencimento, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_pedido = datetime.strptime(valor_data_de_pedido, "%d/%m/%Y").strftime("%Y-%m-%d") #aqui precisamos pegar a data de : data_compra.get que está em valor_data_de_pedido, e converter ela do formato BR para o formato americano, pq o banco de dados lê somente assim
        
        inserir_boleto(valor_nome, data_pedido, float(valor_da_compra), int(valor_parcelas),valor_vencimento_br,)
    
    except ValueError as e:
        print("erro ao converter data", e)        

    
    
    FRM.grid_forget()
    # grid.forget é usado para "esconder" o frame sem perder os widgets que já estavam nele antes
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
    botao_confirmar = Tk.Button(FRM2, text="CONFIRMAR", command=lambda:(enviar_dados(valor_nome,data_pedido,valor_da_compra,valor_parcelas,valor_vencimento_br),checar_e_enviar_boletos() ))
    botao_confirmar.grid(column=4, row=8)  

    botao_voltar = Tk.Button(FRM2, text="VOLTAR", command= (voltar))
    botao_voltar.grid(column=5, row=8) 

    


janela = Tk.Tk()
largura = 650
altura = 400
janela.geometry(f"{largura}x{altura}")

FRM = ttk.Frame(janela, padding=10)
FRM.grid()

FRM2 = ttk.Frame(janela, padding=10)
FRM2.grid()

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
PARCELAS.grid(column=5, row=3)

DATA_VENCIMENTO = Tk.Label(FRM, text="VENCIMENTO")
DATA_VENCIMENTO.grid(column=6, row=3)

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

botao_historico_boletos = Tk.Button(janela, text= "BOLETOS CADASTRADOS", command= visualizacao_tabela)
botao_historico_boletos.place(x=250,y=180)


janela.mainloop()

