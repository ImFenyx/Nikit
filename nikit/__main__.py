tasks = [] # Array vazio de tarefas

def tasklist():
    if tarefas := gettask(tasks): # Se tarefas for diferente de vazio
        print("--- Tarefas ---")
        for tarefa in tarefas:
            print(tarefa)
    main(tasks)

def gettask(tasks): # Função pra puxar tarefas
    return tasks

def main(tasks): # Crud básico
    print("--- Menu ---")
    print("(1) Criar tarefas")
    print("(2) Detalhes das tarefas")
    print("(3) Editar tarefas")
    print("(4) Sair")

    optionmain = input("Escolha uma opção: ")
    if optionmain == "1":
        task = input("Digite a tarefa: ")
        tasks.append(task)
        main(tasks)
    elif optionmain == "2":
        tasklist()
    elif optionmain == "3":
        print("Editar tarefas")
        main(tasks)
    elif optionmain == "4":
        exit()
    else:
        print("Opção inválida")
        main(tasks)

if __name__ == "__main__":
    main(tasks)
