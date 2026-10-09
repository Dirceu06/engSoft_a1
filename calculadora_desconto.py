# Padrão de Projeto: Strategy
# Participantes:
#   EstrategiaDesconto: Strategy
#   DescontoPercentual
#   DescontoFixo      
#   DescontoFidelidade

from abc import ABC, abstractmethod


class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, preco: float, **kwargs) -> float:
        pass


class DescontoPercentual(EstrategiaDesconto):
    def calcular(self, preco: float, valor: float = 0, **kwargs) -> float:
        return max(0.0, preco * (1 - valor / 100))


class DescontoFixo(EstrategiaDesconto):
    def calcular(self, preco: float, valor: float = 0, **kwargs) -> float:
        return max(0.0, preco - valor)


class DescontoFidelidade(EstrategiaDesconto):
    def calcular(self, preco: float, pontos: int = 0, **kwargs) -> float:
        return max(0.0, preco - pontos / 10)


class Calculadora:
    _estrategias = {
        "percentual": DescontoPercentual(),
        "fixo":       DescontoFixo(),
        "fidelidade": DescontoFidelidade(),
    }

    def calcular(self, preco: float, tipo: str, valor: float = 0, pontos: int = 0) -> float:
        estrategia = self._estrategias.get(tipo)
        if estrategia is None:
            return preco
        return estrategia.calcular(preco, valor=valor, pontos=pontos)