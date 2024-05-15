usuarios = []

def verificarUsuario(cpf,usuarios) -> bool:
    usuario_existente = False
    for i in usuarios:
        if i.get("cpf") == cpf:
            usuario_existente = True
        else: 
            usuario_existente = False
    return usuario_existente

def criarUsuario(usuarios) -> None:
    cpf = input("Digite seu cpf: ")
    if verificarUsuario(cpf,usuarios):
        print("Usuário já cadastrado!")
    else:
        nome = input("Digite seu Nome: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Digite seu endereço no formato indicado: \tlogradouro - n° - bairro - cidade/sigla estado\n")
        
        usuarios.append({
            "nome":nome,
            "cpf":cpf,
            "data_nascimento":data_nascimento,
            "endereco":endereco,
            "contas":[],
            })
        
        print("Usuário criado com sucesso!")