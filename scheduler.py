import schedule
import time
import threading
from datetime import datetime, timedelta
from database import ver_boletos
from main import enviar_email
from utils import formatar_data_vencimento

def checar_e_enviar_boletos():
    boletos = ver_boletos()
    HOJE = datetime.today().date()
    
    for boleto in boletos: # aqui fazemos um loop para que percorra todos as tuplas (linhas da tabela) e verifiquem a posição 5
        
        vencimento_str = boleto[5] # aqui pegamos a parte que corresponde ao vencimento na tabela e atribuimos a uma variável que chamamos de vencimento_str      
        vencimento = formatar_data_vencimento(vencimento_str)#aqui convertemos nossa string que está na tabela boletos na  posição 5 em data, para podermos comparar com a data de hoje
        print(f"[DEBUG] Hoje: {HOJE}, vencimento do boleto id {boleto[0]}: {vencimento}, vencimento -1 dia: {vencimento - timedelta(days=1)}")       
        if vencimento is None:
            print(f"erro na data do boleto id{boleto[0]}: {vencimento_str}")
            continue
        if vencimento - timedelta(days=1) == HOJE:
            print(f"lets go enviando aviso de boleto:{boleto}")
            enviar_email(boleto[1], boleto[2], boleto[3], boleto[5])
        else:
            print(f"boleto id {boleto[0]} não vence hoje.")
"""def checagem_diaria():
    schedule.every(5).seconds.do(enviar_email) #aqui será usado para rodar todo dia as 09 da manhã
    while True:
        schedule.run_pending()
        time.sleep(1)
threading.Thread(target=checagem_diaria).start()    

if __name__ == "__main__":
    print("iniciando o scheduler")
    threading.Thread(target=checagem_diaria).start()"""