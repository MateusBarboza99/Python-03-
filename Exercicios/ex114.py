import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO Site não está acessível no momento.\033[m')
else:
    print('\033[34mConsegui acessar o site Pudim com Sucesso!\033[34m')

