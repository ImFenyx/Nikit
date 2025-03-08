tasks = []  # Lista de tarefas

def listar_tarefas():
    if tasks:
        print("\n--- Tarefas ---")
        for indice, tarefa in enumerate(tasks, start=1):
            print(f"{indice}. {tarefa}")

def criar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tasks.append(tarefa)

def editar_tarefa():
    listar_tarefas()
    if tasks:
        try:
            indice = int(input("Digite o número da tarefa para editar: ")) - 1
            if 0 <= indice < len(tasks):
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                tasks[indice] = nova_tarefa
                print("Tarefa editada com sucesso!")
            else:
                print("Número da tarefa inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    while True:
        listar_tarefas()
        print("\n--- Menu ---")
        print("(1) Criar tarefa")
        print("(2) Listar tarefas")
        print("(3) Editar tarefa")
        print("(4) Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            editar_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
