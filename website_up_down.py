import urllib.request
import urllib.error
from lib import*
from time import sleep


cont = 0
error = ''
log = 'Logs.txt'
while cont < 3:
    try:
        site = urllib.request.urlopen('http://pudim.')
        print('\033[0;32mWebsite UP!\033[m')
        break
    except urllib.error.URLError as e:
        error = str(e)
        if cont == 0:
            criar_arquivo(log, error)
        else:
            atualizar_arquivo(log, error)
        sleep(120)
    cont += 1
if cont == 3:
    print('Tentativas de conexão esgotadas.')
    logs_email(log, error)
    # enviar_email(str(error))
