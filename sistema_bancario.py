
#print("**********Menu**********")
#print("Criar Usuário")
#print("Depositar")
#print("Sacar")

#Importação de biblioteca
from datetime import datetime

saldo = 0
limite = 500
numero_saques = 0
limites_saques = 3
usuarios =[]#criei uma lista vazia , pois serão adicionados valores posteriormente
contas = []
agencia='0001'

#Menu com as opções que o usuário vai escolher
def menu():
    print('''
        **********Menu**********
        (1) Criar Usuário
        (2) Criar Conta
        (3) Listar Contas
        (d) Depositar
        (s) Sacar
        (e) Extrato
        (q) Sair
    ''')
    return input('Qual opção deseja')

def deposito(valor,saldo):
    #  vou receber o valor do depósito e somar ao saldo
    if valor > 0 :
        saldo += valor
        #print mostrando o valor depositado
        print(f'Você depositou R${valor}')      
    else:
        print('Valor do deposito Ínválido.Verifique a quantia digitada.')
    
    return saldo

def saque(saque,saldo):


   global  numero_saques,limites,limites_saques
    #De acordo com a documentação Python , váriaveis globais não ficam presas ao limite do escopo da função.
   if numero_saques >= limites_saques:
    print('Você atingiu o limite de saques de sua conta.Tente novamente no proximo dia útil')
   else:
        if saque <= 0:
            print('Saque Inválido.Verifique o valor e tente novamente.')
        elif saque > limite :
            print('Valor limite excedido.Verifique o valor e tente novamente.')
        elif saque > saldo :
            print('Saldo insuficiênte.Verifique o valor e tente novamente.')
        else:
            saldo -= saque
            numero_saques += 1
            
        return saldo   

def extrato (saldo):  
    hora = datetime.now() #Obtem a hora atual 
    horaatual = hora.strftime('%d/%m/%Y/ %H:%M')
    print('=============Extrato=============')
    print(f'{horaatual} \nSaldo disponível:{saldo}' )
    print('\n=============Extrato=============')

def sair():
    print('**********Encerrando o sistema**********')
    
def novo_usuario(usuário):
    cpf = int(input('Digite seu CPF (Somente números);'))
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print('Usuário já cadastrado na base de dados!')
        return

    nome = str('Escreva seu nome completo :')
    data_nascimento = input('Informe a data de nascimento(dd--mm--aa):')
    endereço = input('Informe seu endereço (Rua, Número, CEP, Bairro e Cidade)')

    usuarios.append(f'nome:{nome}, data de nascimento:{data_nascimento}, endereço:{endereço}')
    print('Cadastro realizado com sucesso!')

def filtrar_usuario (cpf,usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuarios
    ['cpf'] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else none