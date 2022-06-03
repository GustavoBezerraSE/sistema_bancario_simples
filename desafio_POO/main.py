from modulos import banco, cliente, conta

banco1 = banco.Banco()

cliente1 = cliente.Cliente('Gustavo', 20)
cliente2 = cliente.Cliente('Pedro', 30)
cliente3 = cliente.Cliente('Carlos', 40)

conta1 = conta.ContaPoupanca(1111, 254136, 0)
conta2 = conta.ContaCorrente(2222, 254137, 0)
conta3 = conta.ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco1.inserir_cliente(cliente1)
banco1.inserir_contas(conta1)

banco1.inserir_cliente(cliente2)
banco1.inserir_contas(conta2)

if banco1.verificacao(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco1.verificacao(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')
