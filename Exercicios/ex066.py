soma = cont = 0
while True:
    núm = int(input('Digite um número [999 para parar]:'))
    if núm == 999:
        break
    cont += 1
    soma += núm
print(f'Foram Digitados {cont} números a soma vale {soma}!')
