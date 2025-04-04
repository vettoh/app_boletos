import smtplib 
from email.mime.text import MIMEText # permite criar o corpo do email ou seja texto
from email.mime.multipart import MIMEMultipart # permite adicionar multipartes no corpo do email, como texto e um anexo por exemplo


class enviar_email: # aqui criamos uma classe que vai encapsular todo o codígo de servidor do email
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
def __init__ (self,email,senha):
    self.email = email
    self.senha = senha # colocar a senha do remetente, existe uma forma de por a senha camuflada aqui, por questões de segurança

def send_email (self, destinatario,assunto,mensagem):
 try: 
    msg = MIMEMultipart
    msg['weverton@htamoveis.com.br'] = self.email
    msg['weverton@htamoveis.com.br'] = destinatario
    msg['ALERTA DE VENCIMENTO DE BOLETO'] = assunto
    msg.attach(MIMEText(mensagem, "plain"))

# conectar ao servidor smtp do gmail 
    server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) #conectamos ao servidor
    server.starttls() # usamos server.starttls para acionar a criptografia tls para tornar o email seguro
    server.login(self.email, self.senha) # fazemos o login com email e senha 

# enviar o email
    server.sendemail(send_email,destinatario,msg.as_string())

# fechar o servidor
    server.quit()

# testando servidor
 except Exception as e:
    print("erro ao enviar email: {e}")

# fazer a parte do emailsender...


