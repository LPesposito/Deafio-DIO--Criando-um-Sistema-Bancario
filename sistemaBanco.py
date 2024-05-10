

conta = {
    'Saldo':1000,
}
extrato = []

def depositar() -> None:
    try:
        valor = float(input("Insira o valor a ser depositado: R$"))
        if valor > 0:
            conta['Saldo'] += valor
            print(f"Deposito no valor de R${valor:.2f} bem sucedido!")
            print(f"Saldo atual R${conta['Saldo']}")
            extrato.append(f'Deposito no valor de R${valor:.2f}')
    except(ValueError):
        print("Por favor insira apenas números!")
        depositar()
    

#função de saque
def sacar() -> None:
    try:
        valor = float(input("Insira o valor a ser sacado: R$"))
        if valor < conta['Saldo'] and valor > 0:
            conta['Saldo'] -= valor
            print(f"Saque bem sucedido no valor de R${valor:.2f}")
            print(f"Saldo atual R${conta['Saldo']}")
            extrato.append(f'Saque no valor de R${valor:.2f}')
        else:
            print(
                f"Não foi possível realizar o saque. Saldo solicidato indisponível! \nValor solicitado: R${valor:.2f} \nSaldo na Conta: R${conta['Saldo']:.2f}"
            )     
    except(ValueError):
        print("Por favor insira apenas números!")
        sacar()
    

#funcao para vizualizar o extrato bancario    
def vizualiar_extrato() -> None:
    if extrato:
        print("===Seu Extrato===")
        for m in extrato:
            print(f"=   {m}")
        print(f"\n=   Saldo atual: R${conta['Saldo']:.2f}")
    else:
        print(f"Não há movimentações! \nSaldo atual: R${conta['Saldo']:.2f}")
        


menu = f"""
[MENU]
[e] Vizualizar Extrato
[d] Depositar
[s] Sacar
[q] Sair
"""
while True:
    opicao = input(menu+'Selecione uma opição: ')
    
    if opicao == 's':
        sacar()
    elif opicao == 'd':
        depositar()
    elif opicao == 'e':
        vizualiar_extrato()
    elif opicao == 'q':
        break
