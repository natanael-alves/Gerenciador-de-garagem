carros =  [
    {
        "placa": "CDC-2026",
        "cor": "Vermelho",
        "modelo": "Corolla",
        "marca" : "Toyota",
        "ano": 2026
    },
    {
        "placa": "OAO-s60i",
        "cor": "Preto",
        "modelo": "Hb20",
        "marca" : "Hyndai",
        "ano" : 2014
    },
    {
        "placa": "QZB-7A52",
        "cor": "Braco",
        "modelo": "S10",
        "marca" : "Chevrolle",
        "ano" : 2025
        
    }
]

def listar_carros ():
    print("\n------------------- LISTA DE CARROS -------------------")

    for carro in carros:
        print(f"Placa: {carro["placa"]} | Modelo: {carro["modelo"]} | Cor: {carro["cor"]} | Ano: {carro["ano"]} | Marca: {carro["marca"]}")

    print("--------------------------------------------------------")

def exibir_menu():
    print("\n----------GERENCIADOR DE GARAGEM----------")
    print("1 - Cadastrar um carro")
    print("2 - Listar os carros existentes")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao_escolhida = input("\nEscolha uma opção: ")

    if opcao_escolhida == "1":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao_escolhida == "2":
        listar_carros()
    elif opcao_escolhida == "3":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao_escolhida == "4":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao_escolhida == "5":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else :
        print("\nOpção inválida. Tente novamente. ")