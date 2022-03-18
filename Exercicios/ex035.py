print('\033[33;1;1m-='*20)
print('\033[4;31;1mAnalisador de Triângulos\033[4;31;1m')
print('\033[33;1;1m-=\033[m'*20)
r1 = float(input('\033[1;34;1mPrimeiro segmento:\033[m '))
r2 = float(input('\033[1;31;1mSegundo segmento:\033[m '))
r3 = float(input('\033[1;35;1mTerceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;30;44mOs segmentos acima PODEM FORMAR TRIÂNGULO!\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')