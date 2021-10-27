while True:
    try:
        cpf = input('Digite um CPF:')
        cpf2 = cpf[:-2]
        soma = 0
        soma_2 = 0
        for p, r in enumerate(range(10, 1, -1)):
            y = int(cpf2[p]) * r
            soma = soma + y
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0
            cpf2 = cpf2 + str(digito)
        else:
            cpf2 = cpf2 + str(digito)

        for p, r in enumerate(range(11, 1, -1)):
            y = int(cpf2[p]) * r
            soma_2 = soma_2 + y

        digito_2 = 11 - (soma_2 % 11)
        cpf2 += str(digito_2)

        sequencia = cpf2 == str(cpf2[0]) * len(cpf)
        if cpf2 == cpf and not sequencia:
            print('CPF Valido!')
        else:
            print('CPF Invalido!')
    except:
        print('CPF digitado invalido digite somente números!')
