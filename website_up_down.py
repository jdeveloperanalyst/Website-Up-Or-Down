import html
from lib import*
import urllib.error
import urllib.request
from time import sleep


cont = 0
error = ''
msg_erro_email = ''
log = 'Logs.txt'
while cont < 3:
    try:
        site = urllib.request.urlopen('http://pudim.')
        print('\033[0;32mWebsite UP!\033[m')
        break
    except urllib.error.URLError as e:
        error = repr(str(e))
        msg_erro_email = html.escape(str(e))
        if cont == 0:
            criar_arquivo(log, error)
        else:
            atualizar_arquivo(log, error)
        sleep(10)
    cont += 1
if cont == 3:
    print('Tentativas de conexão esgotadas.')
    logs_email(log, str(error))
    enviar_email(msg_erro_email)
