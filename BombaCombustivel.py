class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor):
        if valor <= 0:
            print("Valor inválido. O valor deve ser maior que zero.")
            return

        litros_abastecidos = valor / self.valor_litro

        if litros_abastecidos <= self.quantidade_combustivel:
            print(f"Abastecimento de R${valor} realizado.")
            print(f"Foram colocados {litros_abastecidos} litros no veículo.")
            self.quantidade_combustivel -= litros_abastecidos
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def abastecerPorLitro(self, litros):
        if litros <= 0:
            print("Quantidade inválida. A quantidade deve ser maior que zero.")
            return

        valor_a_pagar = litros * self.valor_litro

        if litros <= self.quantidade_combustivel:
            print(f"Abastecimento de {litros} litros realizado.")
            print(f"Valor a pagar: R${valor_a_pagar}")
            self.quantidade_combustivel -= litros
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def alterarValor(self, novo_valor):
        if novo_valor <= 0:
            print("Quantidade deve ser maior que zero.")
        else:
            self.valor_litro = novo_valor
            print(f"Valor do litro alterado para R${novo_valor}")

    def alterarCombustivel(self, combustivel):
        self.tipo_combustivel = combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.quantidade_combustivel = nova_quantidade
            print(f"Quantidade de combustível alterada para {nova_quantidade} litros")
        else:
            print("Quantidade deve ser maior que zero.")
