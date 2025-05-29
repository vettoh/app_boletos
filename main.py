from email_sender import EmailSender
from dotenv import load_dotenv
import os
from pathlib import Path
# usamos dotenv para pode camuflar as senhas na medida que elas fiquem seguras quando formos compartilhar o código

def enviar_email(nome, data_pedido, valor, vencimento):

    dotenv_path = Path('.') / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    email = os.getenv("EMAIL_USER")
    senha = os.getenv("EMAIL_PASS")


    email_service = EmailSender(email,senha)
    email_service.send_email("weverton@htamoveis.com.br", "lembrete de vencimento do boleto", f"seu boleto {nome}, que foi comprado em {data_pedido}, com valor de {valor}, e vencimento em {vencimento}, vence amanhã")

