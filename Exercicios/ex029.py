velocidade = float(input('Qual é a Velocidade Do Seu Carro km/h? '))
if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que é 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    ponto = (velocidade - 85) * 1
    print('E Ganhará {:.0f} pontos na sua CNH, não passando o limite de 80km/h não recebera pontos. '.format(ponto, velocidade))
print('Tenha Um Bom dia! Dirija com Segurança!')







