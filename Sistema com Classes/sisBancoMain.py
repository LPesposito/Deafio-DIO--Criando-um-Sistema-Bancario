import textwrap
from sisBancoClasses import *

def menu():
    print(f"""
    =========[MENU]=========
    [e]\tVizualizar Extrato
    [d]\tDepositar
    [s]\tSacar 
    [q]\tSair
    [nu]\tCriar Usuário
    [cc]\tCriar conta corrente
    """)
    return input('Selecione uma opição: ')

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta!")
        
        return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente:Cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(" Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta:Conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(" \n Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta:Conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf=cpf,clientes=clientes)
    
    if not cliente:
        print(" Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n---------------------[Extrato]---------------------")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("--------------------------------------------------")
    
def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente:Cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\nCliente já cadastrado! Criação de conta cancelada!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço atual: ")
    
    cliente = PessoaFisica(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        endereco=endereco
    )
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente:Cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\nCliente não encontrado! Criação de conta cancelada!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n Conta criada com sucesso!")
    
def listar_constas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
    
def main():
    clientes = []
    contas = []
    
    #main loop
    while True:
        opicao = menu()
        
        if opicao == 's':
            sacar(clientes)
            
            
        elif opicao == 'd':
            depositar(clientes)
            
        elif opicao == 'e':
            exibir_extrato(clientes)
            
        elif opicao == 'nu':
            criar_cliente(clientes)
        
        elif opicao == 'cc':
            numero = len(contas) + 1
            criar_conta(numero,clientes,contas)
            
        elif opicao == 'q':
            break

main()            