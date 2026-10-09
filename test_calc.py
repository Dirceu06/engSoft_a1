# ciclo Vermelho-Verde-Refatorar
# Problema: Calculadora de Desconto
# Casos de teste: desconto percentual, fixo e fidelidade (10 pontos = R$1,00)
# Padrão: Strategy — algoritmos de desconto intercambiáveis em classes separadas
# Uso de IA: Claude auxiliou na estrutura e nos commits

import pytest
from calculadora_desconto import Calculadora


def test_desconto_percentual_10_porcento():
    assert Calculadora().calcular(100.0, tipo="percentual", valor=10) == 90.0

def test_desconto_percentual_zero_nao_altera_preco():
    assert Calculadora().calcular(50.0, tipo="percentual", valor=0) == 50.0

def test_desconto_percentual_50_porcento():
    assert Calculadora().calcular(200.0, tipo="percentual", valor=50) == 100.0

def test_desconto_fixo_subtrai_valor():
    assert Calculadora().calcular(100.0, tipo="fixo", valor=15) == 85.0

def test_desconto_fixo_nao_resulta_em_preco_negativo():
    assert Calculadora().calcular(10.0, tipo="fixo", valor=20) == 0.0

def test_desconto_fixo_zero_nao_altera_preco():
    assert Calculadora().calcular(80.0, tipo="fixo", valor=0) == 80.0

def test_desconto_fidelidade_100_pontos():
    assert Calculadora().calcular(100.0, tipo="fidelidade", pontos=100) == 90.0

def test_desconto_fidelidade_zero_pontos_nao_altera_preco():
    assert Calculadora().calcular(50.0, tipo="fidelidade", pontos=0) == 50.0

def test_desconto_fidelidade_nao_resulta_em_preco_negativo():
    assert Calculadora().calcular(10.0, tipo="fidelidade", pontos=500) == 0.0