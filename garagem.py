carros =  []

def encontrar_carro(placa):
    carro_encontrado = None

    for carro in carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro
            break
    return carro_encontrado

def cadastrar_carro():
    placa =  input("Digite a placa: ").strip()

    if len(placa) == 0:
        print("\nO campo placa não pode ser vazio. ")
        return

    carro_existente = encontrar_carro(placa)
    if carro_existente != None:
        print("\nJá existe um carro cadastrado com essa placa.")
        return


    modelo = input("Digite o modelo: ").strip()
    if len(modelo) == 0:
        print("\nO campo modelo não pode ser vazio. ")
        return
    cor = input("Digite a cor: ").strip()
    if len(cor) == 0:
        print("\nO campo cor não pode ser vazio. ")
        return

    ano = int(input("Digite o ano: "))

    marca = input("Digite a marca: ").strip()
    if len(marca)== 0:
        print("\nO campo marca não pode ser vazio. ")

    carro = {
        "placa": placa,
        "modelo": modelo,
        "cor": cor,
        "ano": ano,
        "marca": marca

    }

    carros.append(carro)
    print("\nCarro cadastrado com êxido")

def listar_carros ():
    print("\n------------------- LISTA DE CARROS -------------------")

    for carro in carros:
        print(f"Placa: {carro["placa"]} | Modelo: {carro["modelo"]} | Cor: {carro["cor"]} | Ano: {carro["ano"]} | Marca: {carro["marca"]}")

    print("--------------------------------------------------------")

def editar_carro():
    placa = input("Digite a placa do carro a ser editado: ").strip()

    carro_existente = encontrar_carro(placa)

    if carro_existente == None:
        print("\nNão foi encontrado um carro com essa placa.")
        return

    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "modelo": carro_existente["modelo"],
        "cor": carro_existente["cor"],
        "ano": carro_existente["ano"],
        "marca": carro_existente["marca"],
    }

    print("\nPressione Enter para manter o valor atual. ")

    nova_placa = input(f"Nova placa (atual: {carro_existente["placa"]}): ").strip()

    if len(nova_placa) > 0:
        if encontrar_carro(nova_placa) != None:
            print("\nJá existe um outro carro com essa placa. ")
            return
        
        dicionario_atualizacao["placa"] = nova_placa

    nova_cor = input(f"Nova cor(atual: {carro_existente["cor"]}): ").strip()
    if len(nova_cor) > 0:
        dicionario_atualizacao["cor"] = nova_cor

    novo_modelo = input(f"Novo modelo (atual: {carro_existente["modelo"]}): ").strip()
    if len(novo_modelo) > 0:
        dicionario_atualizacao["modelo"] = novo_modelo

    novo_ano =(input(f"Novo ano (atual: {carro_existente["ano"]}): ")).strip()
    if len(novo_ano) > 0:
        dicionario_atualizacao["ano"] = (novo_ano)


    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]
    carro_existente["marca"] = dicionario_atualizacao["marca"]

    print("\nCarro editado com êxito. ")

def deletar_carro():
    placa = input("Digite a placa a ser deletada: ").strip()

    carro_retornado = encontrar_carro(placa)

    if carro_retornado == None:
        print("\nNão foi encontrado um carro com essa placa")
        return
    
    carros.remove(carro_retornado)
    print("\nCarro deletado com êxito")

def exibir_menu():
    print("\n----------GERENCIADOR DE GARAGEM----------")
    print("1 - Cadastrar um carro")
    print("2 - Listar os carros existentes")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao_escolhida = input("\nEscolha uma opção: ").strip()

    if opcao_escolhida == "1":
        cadastrar_carro()
    elif opcao_escolhida == "2":
        listar_carros()
    elif opcao_escolhida == "3":
        editar_carro()
    elif opcao_escolhida == "4":
        deletar_carro()
    elif opcao_escolhida == "5":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else :
        print("\nOpção inválida. Tente novamente. ")