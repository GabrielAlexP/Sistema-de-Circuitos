from Modulos import cor
def escolha():
    """
    :return: Circuit system options menu
    """
    print(45*'-=')
    print('CIRCUITOS'.center(90))
    print('-='*45)
    print(f'Bem vindo ao programa! Primeiro vamos identificar, que elemento deseja encontrar ?{cor.cor(0)}')
    print()
    print(f'{cor.cor(cor="amarelo")}[1]{cor.cor(0)} - Resistência')
    print(f'{cor.cor(cor="amarelo")}[2]{cor.cor(0)} - Tensão')
    print(f'{cor.cor(cor="amarelo")}[3]{cor.cor(0)} - Corrente')
    print(f'{cor.cor(cor="amarelo")}[4]{cor.cor(0)} - Teorema da Superposição{cor.cor(0)}')
    print('-='*45)

def resistencia():
    """
    :return: Resistance calculation using Ohm's Law (R = V / i )
    """
    while True:
        try:
            tensao = float(input(f"Digite o valor da tensão em volts {cor.cor(cor='amarelo')}(V):{cor.cor(0)} "))
            break
        except:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    while True:
        try:
            corrente = float(input(f"Digite o valor da corrente em amperes {cor.cor(cor='amarelo')}(A):{cor.cor(0)} "))
            break
        except ValueError:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')

    resistencia = tensao / corrente
    print("{}O valor da resistência é {:.2f} ohms (Ω){}".format(cor.cor(4), resistencia, cor.cor(0)))

def tensão():
    """
    :return:Voltage Calculation using Ohm's Law (V = Rec * i )
    """
    while True:
        try:
            resist_total = 0
            corr = float(input(f'Valor da corrente {cor.cor(cor="amarelo")}(A){cor.cor(0)} ? '))
            break
        except:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    while True:
        try:
            qnt = int(input('Quantos resistores há no circuito ? '))
            break
        except:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    for c in range(1, qnt + 1):
        while True:
            try:
                resist = float(input(f'Valor do {c}° resistor: '))
                resist_total += resist
                break
            except:
                print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    tens = corr * resist_total
    print(f'{cor.cor(cor="azul")}O valor da Tensão é: {tens}.')

def corrente():
    """
    :return: Current calculation using Ohm's Law (i = V / Rec )
    """
    while True:
        try:
            resist_total = 0
            tens = float(input(f'Valor da Tensão em Volts {cor.cor(cor="amarelo")}(V){cor.cor(0)} '))
            break
        except ValueError:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    while True:
        try:
            qnt = int(input('Quantos resistores há no circuito? '))
            break
        except ValueError:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    for c in range(1, qnt + 1):
        while True:
            try:
                resist = float(input(f'Valor do {c}° resistor em ohms {cor.cor(cor="amarelo")}(Ω){cor.cor(0)} '))
                resist_total += resist
                break
            except ValueError:
                print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    corr = tens / resist_total
    print(f'{cor.cor(cor="azul")}O valor da corrente é: {corr:.2f}.{cor.cor(0)}')

def superposicao():
    """
    :return: Theorem of superposition calculation
    """
    while True:
        try:
            fontes_tensao = int(input("Quantas fontes de tensão você deseja usar? "))
            break
        except:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    while True:
        try:
            num_resistores = int(input("Quantos resistores você deseja usar? "))
            break
        except:
            print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
    fontes = []
    resistores = []
    for i in range(fontes_tensao):
        while True:
            try:
                voltagem = float(input("Digite o valor da fonte de tensão em Volts {}(V){} {}: ".format(cor.cor(3), cor.cor(0), i + 1)))
                break
            except:
                print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
        fontes.append(voltagem)
    for i in range(num_resistores):
        while True:
            try:
                resistencia = float(input("Digite o valor da resistência em ohms {}(Ω){} {}: ".format(cor.cor(3), cor.cor(0), i + 1)))
                break
            except:
                print(f'{cor.cor(cor="vermelho")}Insira apenas numeros na lacuna{cor.cor(0)}')
        resistores.append(resistencia)
    Req = sum(resistores)
    for i in range(num_resistores):
        correntes = []
        for j in range(fontes_tensao):
            fonte_ativa = [0] * fontes_tensao
            fonte_ativa[j] = fontes[j]
            voltagem_queda = fonte_ativa[j] * resistores[i] / Req
            corr = voltagem_queda / resistores[i]
            correntes.append(corr)
        total_corr = sum(correntes)
    print("{}A corrente total no resistor é {} A{}".format(cor.cor(4), total_corr, cor.cor(0)))

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
            print(f'{cor.cor(cor="vermelho")}Por favor, insira somente numeros inteiros.{cor.cor(0)}')
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