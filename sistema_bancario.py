#print("********Menu********")
#print("Criar usuário")
#print("Depositar")
#print("Sacar")

saldo = 0
limite = 500
numero_saques = 0
limite_saque = 3
usuario = []
contas = []
agencia = '001'


def menu():
    print('''
    ********Menu********
    (1) Criar usuário
    (2) Criar conta
    (3) Listar contas
    (d) Depositar
    (s) Sacar
    (e) Extrato
    (q) Sair
    ''')
    return input('Qual opção deseja')

def deposito(valor,saldo):

    if valor > 0 :
        saldo += valor

        print(f'Você depositou R${valor}')
    else:
        print('Valor do deposito inválido. Verifique a quatia digitada.')
    return saldo

def saque(saque,saldo):
    global numero_saques,limite_saque
    #de acordo com a documentação python, variaveis globais não ficam presas ao limite do escopo da função.
    if numero_saques >= limite_saque
     print('Você atingiu o limite de saque se dua conta. Tente novamente no proximo dia útil')
    else:
        if saque <= 0:
            print("Saque inválido. Verifique o valor e tente novamente.")
        elif saque > limite :
            print("Valor limite excedido. Verifique o valor e tente novamente.")
        elif saque > saldo :
            print("Saldo insulficiênte. Verifique o valor e tente novamente.")
        else:
            saldo -= saque
            numero_saques += 1
    return saldo