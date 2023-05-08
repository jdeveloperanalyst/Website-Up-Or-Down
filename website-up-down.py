import urllib.request
import urllib.error


try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError as e:
    print('\033[0;31mO Website não está acessível no momento.\033[m')
    print(e)
else:
    print('\033[0;32mWebsite UP!\033[m')
