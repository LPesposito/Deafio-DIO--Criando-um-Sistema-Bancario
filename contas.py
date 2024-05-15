from usuarios import usuarios,criarUsuario
contas = []
       
def criarContaCorrente(contas,agencia,usuarios) -> None:
    try:
        usuario = usuarios[ver_usuarios(usuarios)]
        numero_da_conta = len(contas) + 1
        contas.append({"agencia":agencia,"numero":numero_da_conta,"usuario":usuario.get("cpf")})
        usuario.get("contas").append(numero_da_conta)
        print(f"Nova conta corrente criada com sucesso! \nNúmero da conta: {numero_da_conta}\nAgencia: {agencia}\nUsuário: {usuario.get("nome")}")
    except:
        print("Não foi possivel criar conta corrente!")

def ver_usuarios(lista) -> int:
    user = 0
    if len(lista) > 0:
        print("Escolha um usuário por seu numero: ")
        for i in lista:
            userNum = 0
            print(f"Usuario [{userNum}]: Nome:{i.get("nome")} Cpf:{i.get("cpf")}")
            userNum += 1
        user = int(input("Digite aqui o numero: "))
        return user
        
    else:
        print("Não há usuarios para criar conta corrente!")
        new = input("Criar novo usuario? [s]/[n]: ")
        if new == 's':
            criarUsuario(usuarios)
            return ver_usuarios(usuarios)
        else:
            return -1
    
    
            
    