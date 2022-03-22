peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é sua Altura? (m)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ' '\033[32mABAIXO DO PESO NORMAL\033[m')
elif 18.5 <= imc < 25:
    print('\033[36mPARABÊNS\033[m', 'você está na faixa de ' '\033[34mPESO NORMAL\033[m')
elif 25 <= imc < 30:
    print('Você está em ' '\033[35mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('Você está em ' '\033[33mOBESIDADE\033[m')
elif imc >= 40:
    print('Você está em ' '\033[31mOBESIDADE MÓRBIDA\033[m, cuidado!')


