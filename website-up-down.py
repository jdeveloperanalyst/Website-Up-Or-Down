import urllib.request
import urllib.error
import smtplib


def env_email():
    remetente = ''
    senha = ''
    destinatario = ''

    assunto = ''
    corpo = ''

    mensagem = f'Subject: {assunto}\n\n{corpo}'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, mensagem)
            print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')


try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[0;31mO Website não está acessível no momento.\033[m')
else:
    print('\033[0;32mWebsite UP!\033[m')
