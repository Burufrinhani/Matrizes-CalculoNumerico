# Definindo listas para armazenar o sistema e o sistema escalonado
sistema = []
sistema_escalonado = []
programa = True  # Flag para controlar o loop principal

# Função para criar o sistema de equações
def criar_sistema():
    sistema.clear()  # Limpa a lista sistema antes de criar um novo

    # Entrada do número de linhas e colunas
    linhas = int(input("Digite o número de linhas do sistema: "))
    colunas = int(input("Digite o número de colunas do sistema: "))

    # Preenchendo o sistema com os valores fornecidos pelo usuário
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Digite o número para a posição [{i+1},{j+1}]: ")))
        sistema.append(linha)

# Função para mostrar o sistema original
def mostrar_sistema():
    if not sistema:
        print("Sistema ainda não foi criado, primeiro use a opção 'Criar um sistema' para poder visualizar ele")
        return
    for linha in sistema:
        print("[", ", ".join(map(str, linha)), "]")

# Função para escalonar o sistema usando eliminação de Gauss
def escalonar_sistema():
    sistema_escalonado.clear()  # Limpa o sistema escalonado antes de usar

    if not sistema:
        print("Sistema ainda não foi criado, primeiro use a opção 'Criar um sistema' para poder escalonar ele")
        return
    
    # Criar uma cópia do sistema original
    sistema_escalonado.extend([linha[:] for linha in sistema])

    linhas = len(sistema_escalonado)
    colunas = len(sistema_escalonado[0])
    
    for i in range(linhas):
        if sistema_escalonado[i][i] == 0:
            for k in range(i+1, linhas):
                if sistema_escalonado[k][i] != 0:
                    sistema_escalonado[i], sistema_escalonado[k] = sistema_escalonado[k], sistema_escalonado[i]
                    break
            else:
                print("O sistema pode não ter solução ou ter infinitas soluções.")
                return
        
        for j in range(i+1, linhas):
            fator = sistema_escalonado[j][i] / sistema_escalonado[i][i]
            for k in range(i, colunas):
                sistema_escalonado[j][k] -= fator * sistema_escalonado[i][k]

# Função para mostrar o sistema escalonado
def mostrar_sistema_escalonado():
    if not sistema_escalonado:
        print("Sistema escalonado ainda não foi criado, primeiro use a opção 'Escalonar sistema' para poder visualizar ele")
        return
    for linha in sistema_escalonado:
        print("[", ", ".join(map(str, linha)), "]")

# Função para calcular a solução do sistema
def solucao():
    if not sistema_escalonado:
        print("Sistema escalonado ainda não foi criado, primeiro use a opção 'Escalonar sistema' para poder visualizar ele")
        return

    linhas = len(sistema_escalonado)
    solucao = [0] * linhas

    for i in range(linhas-1, -1, -1):
        soma = sum(sistema_escalonado[i][j] * solucao[j] for j in range(i+1, linhas))
        solucao[i] = (sistema_escalonado[i][-1] - soma) / sistema_escalonado[i][i]
    
    solucao = [round(valor, 2) for valor in solucao]
    print("Solução do sistema: ", solucao)

# Loop do menu
while programa:
    opcao = int(input("\n1- Criar um sistema\n2- Ver o sistema\n3- Escalonar sistema\n4- Mostrar sistema escalonado\n5- Mostrar a solução do sistema\n0- Sair\n"))
    
    match opcao:
        case 1:
            criar_sistema()
        case 2:
            mostrar_sistema()
        case 3:
            escalonar_sistema()
        case 4:
            mostrar_sistema_escalonado()
        case 5:
            solucao()
        case 0:
            programa = False
