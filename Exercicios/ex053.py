#frase = str(input('Digite uma Frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto)-1, -1, -1):
   # inverso += junto[letra]
#print('O inverso de {} é {}'.format(junto, inverso))
#if inverso == junto:
    #print('Temos um PALINDROMO!')
#else:
    #print('A frase digitada NÃO é um PALINDROMO!')


frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada NÃO é um PALINDROMO!')




