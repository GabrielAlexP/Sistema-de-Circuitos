def escolha():
    """
    :return: Circuit system options menu
    """
    print(45*'-=')
    print('CIRCUITOS'.center(90))
    print('-='*45)
    print('Bem vindo ao programa! Primeiro vamos identificar, que elemento deseja encontrar ?')
    print()
    print('[1] - Resistência')
    print('[2] - Tensão')
    print('[3] - Corrente')
    print('[4] - Teorema da Superposição')
    print('-='*45)

def resistencia():
    """
    :return: Resistance calculation using Ohm's Law (R = V / i )
    """
    while True:
        try:
            tensao = float(input("Digite o valor da tensão em volts (V): "))
            break
        except:
            print('Insira apenas numeros na lacuna')
    while True:
        try:
            corrente = float(input("Digite o valor da corrente em amperes (A): "))
            break
        except ValueError:
            print('Insira apenas numeros na lacuna')

    resistencia = tensao / corrente
    print("O valor da resistência é {:.2f} ohms (Ω)".format(resistencia))

def tensão():
    """
    :return:Voltage Calculation using Ohm's Law (V = Rec * i )
    """
    while True:
        try:
            resist_total = 0
            corr = float(input(f'Valor da corrente (A) ? '))
            break
        except:
            print(f'Insira apenas numeros na lacuna')
    while True:
        try:
            qnt = int(input('Quantos resistores há no circuito ? '))
            break
        except:
            print(f'Insira apenas numeros na lacuna')
    for c in range(1, qnt + 1):
        while True:
            try:
                resist = float(input(f'Valor do {c}° resistor: '))
                resist_total += resist
                break
            except:
                print(f'Insira apenas numeros na lacuna')
    tens = corr * resist_total
    print(f'O valor da Tensão é: {tens}.')

def corrente():
    """
    :return: Current calculation using Ohm's Law (i = V / Rec )
    """
    while True:
        try:
            resist_total = 0
            tens = float(input(f'Valor da Tensão em Volts (V) '))
            break
        except ValueError:
            print(f'Insira apenas numeros na lacuna')
    while True:
        try:
            qnt = int(input('Quantos resistores há no circuito? '))
            break
        except ValueError:
            print(f'Insira apenas numeros na lacuna')
    for c in range(1, qnt + 1):
        while True:
            try:
                resist = float(input(f'Valor do {c}° resistor em ohms (Ω) '))
                resist_total += resist
                break
            except ValueError:
                print(f'Insira apenas numeros na lacuna')
    corr = tens / resist_total
    print(f'O valor da corrente é: {corr:.2f}.')

def superposicao():
    """
    :return: Theorem of superposition calculation
    """
    while True:
        try:
            fontes_tensao = int(input("Quantas fontes de tensão você deseja usar? "))
            break
        except ValueError:
            print('Insira apenas números na lacuna')

    while True:
        try:
            num_resistores = int(input("Quantos resistores você deseja usar? "))
            break
        except ValueError:
            print('Insira apenas números na lacuna')

    fontes = []
    resistores = []

    for i in range(fontes_tensao):
        while True:
            try:
                voltagem = float(input(f"Digite o valor da fonte de tensão em Volts {i + 1} (V): "))
                break
            except ValueError:
                print('Insira apenas números na lacuna')
        fontes.append(voltagem)

    for i in range(num_resistores):
        while True:
            try:
                resistencia = float(input(f"Digite o valor da resistência em ohms {i + 1} (Ω): "))
                break
            except ValueError:
                print('Insira apenas números na lacuna')
        resistores.append(resistencia)

    Req = sum(resistores)
    total_corr = 0

    for i in range(num_resistores):
        correntes = []
        for j in range(fontes_tensao):
            fonte_ativa = [0] * fontes_tensao
            fonte_ativa[j] = fontes[j]
            voltagem_queda = fonte_ativa[j] * resistores[i] / Req
            corr = voltagem_queda / resistores[i]
            correntes.append(corr)
        total_corr += sum(correntes)

    print(f"A corrente total no resistor é {total_corr} A")


def perg():
    """
    :return: Menu Responde using the if statement to define wich of the 4 options will be chosen.
    """
    escolha()
    while True:
        try:
            perg = int(input('Qual opção deseja ? '))
            print('-='*45)
            break
        except:
            print(f'Por favor, insira somente numeros inteiros.')
            print('-='*45)
    while True:
        if perg == 1:
            resistencia()
            print('-='*45)
            break
        elif perg == 2:
            tensão()
            print('-=' * 45)
            break
        elif perg == 3:
            corrente()
            print('-=' * 45)
            break
        elif perg == 4:
            superposicao()
            print('-=' * 45)
            break
        else:
            print('Por favor, insira um número válido')

perg()
