import urllib.request
import urllib.error
from enviar_email import enviar_email

cont = 0
try:
    site = urllib.request.urlopen('http://pudim.')
except urllib.error.URLError as e:
    # enviar_email(str(e))
    print(e)
else:
    print('\033[0;32mWebsite UP!\033[m')
