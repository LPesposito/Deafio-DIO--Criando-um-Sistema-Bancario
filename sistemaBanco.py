from contas import contas,criarContaCorrente
from usuarios import usuarios,criarUsuario

#função de deposito
def depositar(saldo,extrato) -> None:
    try:
        valor = float(input("Insira o valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            print(f"Deposito no valor de R${valor:.2f} bem sucedido!")
            print(f"Saldo atual R${saldo}")
            extrato.append(f'Deposito no valor de R${valor:.2f}')
            return saldo
    except(ValueError):
        print("Por favor insira apenas números!")
        depositar()
    

#função de saque
def sacar(*,saldo,extrato,limite_saque,numero_saque,limite):
    try:
        if numero_saque < limite_saque:
            valor = float(input("Insira o valor a ser sacado: R$"))
            if (valor <= saldo) and (valor > 0) and (valor < limite):
                saldo -= valor
                print(f"Saque bem sucedido no valor de R${valor:.2f}")
                print(f"Saldo atual R${saldo}")
                extrato.append(f'Saque no valor de R${valor:.2f}')
                numero_saque += 1 
                return saldo, numero_saque
            else:
                print(
                    f"Não foi possível realizar o saque. Saldo solicidato indisponível! \nValor solicitado: R${valor:.2f} \nSaldo na Conta: R${saldo:.2f}"
                )
                return saldo, numero_saque
    except(ValueError):
        print("Por favor insira apenas números!")
        sacar()
    

#funcao para vizualizar o extrato bancario    
def vizualiar_extrato(saldo,*,extrato) -> None:
    if extrato:
        print("=========Seu Extrato=========")
        for m in extrato:
            print(f"=   {m}")
        print(f"\n=   Saldo atual: R${saldo:.2f}")
    else:
        print(f"Não há movimentações! \nSaldo atual: R${saldo:.2f}")
        


menu = f"""
=========[MENU]=========
[e]\tVizualizar Extrato
[d]\tDepositar
[s]\tSacar 
[q]\tSair
[nu]\tCriar Usuário
[cc]\tCriar conta corrente
"""

def main():
    
    AGENCIA = '0001'
    LIMITE_SAQUE = 3
        
    limite=500
    extrato = []
    saldo = 10
    limite_saque=LIMITE_SAQUE
    numero_saque = 0
    
    while True:
        opicao = input(menu+'Selecione uma opição: ')
        
        if opicao == 's':
            saldo, numero_saque = sacar(saldo=saldo,extrato=extrato,limite_saque=limite,limite=limite,numero_saque=numero_saque)
            
            
        elif opicao == 'd':
            saldo = depositar(saldo,extrato)
            
        elif opicao == 'e':
            vizualiar_extrato(saldo,extrato=extrato)
            
        elif opicao == 'nu':
            criarUsuario(usuarios)
        
        elif opicao == 'cc':
            criarContaCorrente(contas,AGENCIA,usuarios)
            
        elif opicao == 'q':
            break

main()