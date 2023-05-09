import smtplib
import email.message
from credenciais import*


def enviar_email(mensagem_erro=''):
    corpo_email = f"""
    <p>\033[0;31mWebsite fora do ar!!!\033[m</p>
    <p>Erro: {mensagem_erro}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Website Down"
    msg['From'] = credentials['user']
    msg['To'] = credentials['user']
    password = credentials['password']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
