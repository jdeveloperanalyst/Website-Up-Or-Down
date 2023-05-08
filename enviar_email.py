from credenciais import *
import smtplib


def env_email():
    remetente = credentials[0]
    senha = credentials[1]
    destinatario = credentials[0]
    assunto = 'Website Down'
    corpo = '''
    Web site http://pudim.com.br/ fora do ar!
    
    Favor verificar.
    
    Att.
    '''
    mensagem = f'Subject: {assunto}\n\n{corpo}'
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, mensagem)
            print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')
