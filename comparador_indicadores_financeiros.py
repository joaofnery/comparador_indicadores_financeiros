nacoes = int(input('Qual a quantidade de Ações/FIIs deseja comparar? '))
ind1 = str(input('Qual será o primeiro indicador? ')).strip()
ind2 = str(input('Qual será o segundo indicador? ')).strip()
ind3 = str(input('Qual será o terceiro indicador? ')).strip()
listaacao = []
listavalor1 = []
listavalor2 = []
listavalor3 = []
media0 = 0
media1 = 0
media2 = 0
for n in range(1, nacoes + 1):
    acao = str(input('Informe a Ação/FII [{}]: '.format(n)))
    valor1 = float(input('Qual o {}, de {}.'.format(ind1, acao)))
    valor2 = float(input('Qual o {}, de {}. '.format(ind2, acao)))
    valor3 = float(input('Qual o {}, de {}. '.format(ind3, acao)))
    listaacao.append(acao)
    listavalor1.append(valor1)
    listavalor2.append(valor2)
    listavalor3.append(valor3)

if listavalor1[0] > listavalor1[1]:
    media0 += 1
    media1 += 2
elif listavalor1[1] > listavalor1[0]:
    media0 += 2
    media1 += 1

if listavalor2[0] > listavalor2[1]:
    media0 += 1
    media1 += 2
elif listavalor2[1] > listavalor2[0]:
    media0 += 2
    media1 += 1

if listavalor3[0] > listavalor3[1]:
    media0 += 1
    media1 += 2
elif listavalor3[1] > listavalor3[0]:
    media0 += 2
    media1 += 1

print(media0, media1)