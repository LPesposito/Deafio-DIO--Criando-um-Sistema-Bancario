saldo = 1000
extrato = []

#função de deposito
def depositar() -> None:
    global saldo
    try:
        
        valor = float(input("Insira o valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            print(f"Deposito no valor de R${valor:.2f} bem sucedido!")
            print(f"Saldo atual R${saldo}")
            extrato.append(f'Deposito no valor de R${valor:.2f}')
    except(ValueError):
        print("Por favor insira apenas números!")
        depositar()
    

#função de saque
def sacar() -> None:
    global saldo
    try:
        valor = float(input("Insira o valor a ser sacado: R$"))
        if valor < saldo and valor > 0:
            saldo -= valor
            print(f"Saque bem sucedido no valor de R${valor:.2f}")
            print(f"Saldo atual R${saldo}")
            extrato.append(f'Saque no valor de R${valor:.2f}')
        else:
            print(
                f"Não foi possível realizar o saque. Saldo solicidato indisponível! \nValor solicitado: R${valor:.2f} \nSaldo na Conta: R${saldo:.2f}"
            )     
    except(ValueError):
        print("Por favor insira apenas números!")
        sacar()
    

#funcao para vizualizar o extrato bancario    
def vizualiar_extrato() -> None:
    global saldo
    if extrato:
        print("===Seu Extrato===")
        for m in extrato:
            print(f"=   {m}")
        print(f"\n=   Saldo atual: R${saldo:.2f}")
    else:
        print(f"Não há movimentações! \nSaldo atual: R${saldo:.2f}")
        


menu = f"""
[MENU]
[e] Vizualizar Extrato
[d] Depositar
[s] Sacar 
[q] Sair
"""

limite_saque = 3

while True:
    opicao = input(menu+'Selecione uma opição: ')
    
    if opicao == 's':
        if limite_saque > 0:
            limite_saque -= 1 
            sacar()
            print(f"Saques disponíveis: {limite_saque}")
        else:
            print("Limite de saque diário excedido!")
        
        
    elif opicao == 'd':
        depositar()
        
    elif opicao == 'e':
        vizualiar_extrato()
        
    elif opicao == 'q':
        break
