nacoes = int(input('Qual a quantidade de Ações/FIIs deseja comparar? '))
ind1 = str(input('Qual será o primeiro indicador? ')).strip()
ind2 = str(input('Qual será o segundo indicador? ')).strip()
ind3 = str(input('Qual será o terceiro indicador? ')).strip()
acao = []
valor1 = []
valor2 = []
valor3 = []

for n in range(1, nacoes + 1):
    acao[n] = str(input('Informe a Ação/FII [{}]: '.format(n)))
    valor1[n] = float(input('Qual o {}, de {}.'.format(ind1, acao[n])))
    valor2[n] = float(input('Qual o {}, de {}. '.format(ind2, acao[n])))
    valor3[n] = float(input('Qual o {}, de {}. '.format(ind3, acao[n])))
    print(acao, valor1, valor2, valor3)