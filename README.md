# Envio de E-mails Personalizados com Python

Este repositório contém um script em Python para enviar e-mails personalizados para uma lista de destinatários. O script utiliza a biblioteca `smtplib` para enviar e-mails através do servidor SMTP do Gmail e é configurado para enviar uma mensagem de agradecimento para pessoas que se inscreveram em um curso, mas não foram selecionadas.

## 📝 Funcionalidades

- Envia e-mails personalizados para cada destinatário.
- Utiliza o servidor SMTP do Gmail.
- Atraso aleatório entre os envios para evitar que sejam marcados como spam.
- Permite personalizar o corpo do e-mail para cada destinatário usando um modelo.

## 🚀 Como Usar

### 1. Requisitos

Antes de começar, certifique-se de que você tem o Python instalado. As bibliotecas `smtplib`, `email.mime`, e `time` são parte da biblioteca padrão do Python e não precisam ser instaladas separadamente.

### 2. Instalação

Clone este repositório:

```bash
git clone https://github.com/sayydaviid/NoSpamEmail
```

### 3. Configuração

Abra o arquivo envio_email.py e substitua as seguintes informações:

```bash
# Substitua pelas suas credenciais
EMAIL = 'seu_email@gmail.com'  # Insira o seu endereço de e-mail do Gmail
SENHA = 'sua_senha_de_aplicativo'  # Insira a senha de aplicativo gerada
``` 
⚠️ Nota: Para usar o Gmail, você deve gerar uma senha de aplicativo:
1.  Vá para Sua Conta Google.
2.  Habilite a autenticação em duas etapas.
3.   Vá até "Senhas de Aplicativo" e gere uma senha para usar no script.

### 4. Lista de Destinatários

A lista de destinatários está definida na variável lista_destinatarios como uma lista de dicionários, cada um contendo o nome e o e-mail de uma pessoa. Modifique a lista conforme necessário:

```bash
lista_destinatarios = [
    {"nome": "Pedro queixada", "email": "pedroca@gmail.com"},
    {"nome": "Lucas açaí", "email": "luquinhas@gmail.com"},
    {"nome": "Wendell lira", "email": "windows3@gmail.com"},
    # Adicione outros destinatários conforme necessário
]
```
### 5. Execução

Pode-se executar o script no terminal:
Isso enviará um e-mail para cada destinatário na lista, de forma individual, e aguardará um tempo aleatório entre 1 a 5 segundos para cada envio, reduzindo a chance de ser marcado como spam.
### 📄 Estrutura do Código
Configuração do Servidor SMTP

```bash
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'seu_email@gmail.com'  # Substitua pelo seu e-mail do Gmail
SENHA = 'sua_senha_de_aplicativo'  # Substitua pela sua senha de aplicativo gerada
```
O script se conecta ao servidor SMTP do Gmail, utilizando TLS para garantir a segurança do envio dos e-mails.
Modelo de E-mail

O modelo de e-mail (CORPO_TEMPLATE) é usado para personalizar o conteúdo para cada destinatário:

```bash
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
```
### Envio dos E-mails

O código cria um e-mail para cada destinatário usando MIMEMultipart, personaliza o conteúdo, e então envia usando server.sendmail(). A cada envio, o script espera um tempo aleatório entre 1 e 5 segundos.
```bash
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
```
### Fechamento da Conexão

Após todos os e-mails serem enviados, o script fecha a conexão com o servidor SMTP:
```bash
server.quit()
```
### 🔒 Segurança

  * Nunca compartilhe sua senha diretamente no código. Utilize variáveis de ambiente ou arquivos de configuração para armazenar informações sensíveis.
  * Senha de Aplicativo: Sempre utilize a "senha de aplicativo" do Gmail, não a senha pessoal da sua conta, para evitar comprometer sua conta.

### 🛠️ Melhorias Futuras

  * Implementar um sistema para enviar os e-mails de forma assíncrona, melhorando a eficiência do envio.
*  Adicionar tratamento para controlar o limite de envios do Gmail.
  * Armazenar informações sensíveis (e-mail e senha) de forma segura utilizando variáveis de ambiente.
