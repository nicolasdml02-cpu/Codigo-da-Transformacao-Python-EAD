# Criando a exceção personalizada que herda de Exception
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        super().__init__(f"Tentativa de sacar R${valor_saque:.2f}, mas o saldo é de apenas R${saldo_atual:.2f}.")

class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor: float):
        if valor > self.saldo:
            # Lança a exceção criada
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado! Saldo restante: R${self.saldo:.2f}")


# Testando a classe e o tratamento de erro
if __name__ == "__main__":
    minha_conta = ContaBancaria(titular="Carlos", saldo_inicial=100.0)

    try:
        minha_conta.depositar(50.0)
        minha_conta.sacar(30.0)
        # Tentando sacar mais do que possui
        minha_conta.sacar(200.0)
    except SaldoInsuficienteError as erro:
        print(f"\n[EXCEÇÃO CAPTURADA] {erro}")