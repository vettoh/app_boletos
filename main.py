from email_sender import EmailSender
from dotenv import load_dotenv
import os

# usamos dotenv para pode camuflar as senhas na medida que elas fiquem seguras quando formos compartilhar o código
from pathlib import Path
dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)

email = os.getenv("EMAIL_USER")
senha = os.getenv("EMAIL_PASS")

print ("email : ", email )
print ("senha : ", senha )

email_service = EmailSender(email,senha)
email_service.send_email("weverton@htamoveis.com.br", "lembrete de vencimento de boleto", "seu boleto vence amanhã")