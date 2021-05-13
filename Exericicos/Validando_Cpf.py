while True:
    cpf = str(input('Cpf:'))
    novo_cpf = cpf[:-2]
    to = 0
    to2 = 0
    reverso = 11
    reverso2 = 11

    for n in novo_cpf:
        reverso -= 1
        if reverso < 2:
            break
        to += int(n) * reverso
    a = 11 - (to % 11)
    if a > 9:
        a = 0
    else:
        a = a

    novo_cpf += str(a)

    for n2 in novo_cpf:
        to2 += int(n2) * reverso2
        reverso2 -= 1
    a2 = 11 - (to2 % 11)
    novo_cpf += str(a2)

    if cpf == novo_cpf:
        print('VÁLIDO')
    else:
        print('NÃO É VÁLIDO')
    continue
