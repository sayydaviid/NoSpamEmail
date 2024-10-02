import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import random

# Configurações do servidor de email Gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'seu_email@gmail.com'  # Substitua pelo seu email do Gmail
SENHA = 'sua_senha_de_aplicativo'  # Substitua pela sua senha de aplicativo gerada

# Lista de destinatários com nomes e e-mails
lista_destinatarios = [
    {"nome": "Pedro queixada", "email": "pedroca@gmail.com"},
    {"nome": "Lucas açaí", "email": "luquinhas@gmail.com"},
    {"nome": "Wendell lira", "email": "windows3@gmail.com"},
    # Adicione outros destinatários conforme necessário
]

# Assunto e corpo do e-mail
ASSUNTO = "Agradecimento pela Inscrição no Curso 'Pentest & DevOps' - UFPA 2024"
CORPO_TEMPLATE = """
Prezada(o) {nome},

Agradecemos o seu interesse e inscrição no curso "Pentest & DevOps" da Universidade Federal do Pará (UFPA) 2024.

Infelizmente, nesta ocasião, você não foi selecionado(a) para participar do curso. No entanto, gostaríamos de enfatizar que esta é apenas a primeira de muitas oportunidades que virão. Estamos planejando futuros eventos e atividades semelhantes, e gostaríamos muito de contar com a sua participação.

Não desista! Continue acompanhando nossos canais de comunicação para futuras oportunidades. Temos certeza de que haverá outras ocasiões em que poderemos trabalhar juntos.

Caso tenha alguma dúvida ou queira mais informações, sinta-se à vontade para responder este e-mail.

Atenciosamente,
Organização do Curso "Pentest & DevOps"
Universidade Federal do Pará (UFPA)
"""

# Configuração do servidor
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL, SENHA)

# Envio dos emails
for destinatario in lista_destinatarios:
    nome = destinatario['nome']
    email = destinatario['email']
    
    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = email
    msg['Subject'] = ASSUNTO
    
    # Personalização do corpo do e-mail
    corpo_personalizado = CORPO_TEMPLATE.format(nome=nome)
    msg.attach(MIMEText(corpo_personalizado, 'plain'))

    # Enviando o e-mail
    try:
        server.sendmail(EMAIL, email, msg.as_string())
        print(f"E-mail enviado para {nome} - {email}")
    except Exception as e:
        print(f"Falha ao enviar para {nome} - {email}: {e}")

    # Aguardar um tempo aleatório para evitar ser marcado como spam
    time.sleep(random.uniform(1, 5))  # Espera entre 1 e 5 segundos

# Fechar a conexão com o servidor
server.quit()
