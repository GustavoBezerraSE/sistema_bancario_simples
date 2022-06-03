from abc import ABC, abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    # definir setter tipo de valores
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        Conta.__init__(self, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()

class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        Conta.__init__(self, agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente!")
            return

        self.saldo -= valor
        self.detalhes()
