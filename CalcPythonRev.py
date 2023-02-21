def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divisao(x, y):
    return x + y


print("\n******************* Python Calculator *******************")

print("Selecione o número da operação desejada:")

print ("#############################################")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

print ("#############################################")

selecao = int(input("Digite sua opção (1/2/3/4): "))

if selecao == 1:
    primeiroNumero = int(input("Digite o primeiro numero: "))
    segundoNumero = int(input("Digite o segundo numero: "))
    print (primeiroNumero, "+", segundoNumero, "=", soma(primeiroNumero, segundoNumero))  
    
elif selecao == 2:
    primeiroNumero = int(input("Digite o primeiro numero: "))
    segundoNumero = int(input("Digite o segundo numero: "))
    print (primeiroNumero, "-", segundoNumero, "=", subtracao(primeiroNumero, segundoNumero))
           
elif selecao == 3:
    primeiroNumero = int(input("Digite o primeiro numero: "))
    segundoNumero = int(input("Digite o segundo numero: "))
    print (primeiroNumero, "*", segundoNumero, "=", multiplica(primeiroNumero, segundoNumero))
           
           
elif selecao == 4:
    primeiroNumero = int(input("Digite o primeiro numero: "))
    segundoNumero = int(input("Digite o segundo numero: "))
    print (primeiroNumero, "/", segundoNumero, "=", divisao(primeiroNumero, segundoNumero))
    
else:
    primeiroNumero = int(input("Digite o primeiro numero: "))
    segundoNumero = int(input("Digite o segundo numero: "))
    print ("Opção Inválida")

print ("#############################################")

print ("Operação concluída")