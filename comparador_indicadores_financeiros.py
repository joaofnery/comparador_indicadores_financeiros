nacoes = int(input('Qual a quantidade de Ações que deseja comparar? (até 3) '))
ind1 = 'Dividend Yeld'
ind2 = 'P/L'
ind3 = 'P/VP'
listaacao = []
listavalor1 = []
listavalor2 = []
listavalor3 = []
media0 = 0
media1 = 0
media2 = 0
for n in range(1, nacoes + 1):
    acao = str(input('Informe a Ação [{}]: '.format(n)))
    valor1 = float(input('Qual o {}, de {}.'.format(ind1, acao)))
    valor2 = float(input('Qual o {}, de {}. '.format(ind2, acao)))
    valor3 = float(input('Qual o {}, de {}. '.format(ind3, acao)))
    listaacao.append(acao)
    listavalor1.append(valor1)
    listavalor2.append(valor2)
    listavalor3.append(valor3)

if nacoes == 2:

    if listavalor1[0] > listavalor1[1]:
        media0 += 1
        media1 += 2
    elif listavalor1[1] > listavalor1[0]:
        media0 += 2
        media1 += 1

    if listavalor2[0] < listavalor2[1]:
        media0 += 1
        media1 += 2
    elif listavalor2[1] < listavalor2[0]:
        media0 += 2
        media1 += 1

    if listavalor3[0] < listavalor3[1]:
        media0 += 1
        media1 += 2
    elif listavalor3[1] < listavalor3[0]:
        media0 += 2
        media1 += 1

    if media0 < media1:
        print('[1] {}         [2] {}'.format(listaacao[0], listaacao[1]))
    elif media1 < media0:
        print('[1] {}         [2] {}'.format(listaacao[1], listaacao[0]))

elif nacoes == 3:

    if listavalor1[0] > listavalor1[1] > listavalor1[2]:
        media0 += 1
        media1 += 2
        media2 += 3

    elif listavalor1[0] > listavalor1[2] > listavalor1[1]:
        media0 += 1
        media1 += 3
        media2 += 2

    elif listavalor1[1] > listavalor1[0] > listavalor1[2]:
        media0 += 2
        media1 += 1
        media2 += 3

    elif listavalor1[1] > listavalor1[2] > listavalor1[0]:
        media0 += 3
        media1 += 1
        media2 += 2

    elif listavalor1[2] > listavalor1[0] > listavalor1[1]:
        media0 += 2
        media1 += 3
        media2 += 1

    elif listavalor1[2] > listavalor1[1] > listavalor1[0]:
        media0 += 3
        media1 += 2
        media2 += 1

    if listavalor2[0] < listavalor2[1] < listavalor2[2]:
        media0 += 1
        media1 += 2
        media2 += 3

    elif listavalor2[0] < listavalor2[2] < listavalor2[1]:
        media0 += 1
        media1 += 3
        media2 += 2

    elif listavalor2[1] < listavalor2[0] < listavalor2[2]:
        media0 += 2
        media1 += 1
        media2 += 3

    elif listavalor2[1] < listavalor2[2] < listavalor2[0]:
        media0 += 3
        media1 += 1
        media2 += 2

    elif listavalor2[2] < listavalor2[0] < listavalor2[1]:
        media0 += 2
        media1 += 3
        media2 += 1

    elif listavalor2[2] < listavalor2[1] < listavalor2[0]:
        media0 += 3
        media1 += 2
        media2 += 1

    if listavalor3[0] < listavalor3[1] < listavalor3[2]:
        media0 += 1
        media1 += 2
        media2 += 3

    elif listavalor3[0] < listavalor3[2] < listavalor3[1]:
        media0 += 1
        media1 += 3
        media2 += 2

    elif listavalor3[1] < listavalor3[0] < listavalor3[2]:
        media0 += 2
        media1 += 1
        media2 += 3

    elif listavalor3[1] < listavalor3[2] < listavalor3[0]:
        media0 += 3
        media1 += 1
        media2 += 2

    elif listavalor3[2] < listavalor3[0] < listavalor3[1]:
        media0 += 2
        media1 += 3
        media2 += 1

    elif listavalor3[2] < listavalor3[1] < listavalor3[0]:
        media0 += 3
        media1 += 2
        media2 += 1

    if media0 < media1 < media2:
        print('[1] {}         [2] {}        [3] {}'.format(listaacao[0], listaacao[1], listaacao[2]))
        
    elif media0 < media2 < media1:
        print('[1] {}         [2] {}        [3] {}'.format(listaacao[0], listaacao[2], listaacao[1]))

    elif media1 < media0 < media2:
        print('[1] {}         [2] {}        [3] {}'.format(listaacao[1], listaacao[0], listaacao[2]))

    elif media1 < media2 < media0:
        print('[1] {}         [2] {}        [3] {}'.format(listaacao[1], listaacao[2], listaacao[0]))

    elif media2 < media0 < media1:
        print('[1] {}         [2] {}        [3] {}'.format(listaacao[2], listaacao[0], listaacao[1]))

    elif media2 < media1 < media0:
        print('[1] {}         [2] {}        [3] {}'.format(listaacao[2], listaacao[1], listaacao[0]))
