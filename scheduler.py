import schedule
import time
import threading
from datetime import datetime
from database import ver_boletos

def checar_e_enviar_boletos():
    boletos = ver_boletos()
    HOJE = datetime.today().date()
    
    for boleto in boletos: # aqui fazemos um loop para que percorra todos as tuplas (linhas da tabela) e verifiquem a posição 5
        vencimento_str = boleto[5] # aqui pegamos a parte que corresponde ao vencimento na tabela e atribuimos a uma variável que chamamos de vencimento_str
        
        try :
            if "/" in vencimento_str:
                vencimento = datetime.strptime(vencimento_str, "%d/%m/%Y").date() #aqui convertemos nossa string que está na tabela boletos na  posição 5 em data, para podermos comparar com a data de hoje
            else:
                vencimento = datetime.strptime(vencimento_str, "%Y/%m/%d").date()
        except ValueError:
            print(f"erro ao converter boleto: {vencimento_str}")
            continue # pula o boleto em questão se a data estiver errada

        if vencimento == HOJE:
            print(f"boleto de {boleto[1]} vence hoje")

        else:
            print("boleto não vence hoje")