#requisitos a ser implementados
# - (usuário) deve mostrar quais vagas disponíveis no estacionamento em tempo real
# - (usuário) deve impedir ocupação de vagas que requerem autorização

import estacionamento
from estacionamento import vagas

vagas_class = estacionamento.Estacionamento()

print("vagas disponíveis: ", vagas(vagas_class))  # Mostrar vagas disponíveis
#interação com o usuário para ocupar uma vaga
c = input("Digite o número da vaga que deseja ocupar: ")
c = int(c)
# tem autorização para ocupar a vaga?

r = input("Você tem autorização para ocupar a vaga? (s/n): ")
autorizado = r.lower() == 's'


# tentando ocupar a vaga
# estacionamento.ocupar_vaga(vagas_class, c, autorizado)
if vagas_class.ocupar_vaga(c, autorizado):
    print(f"Vaga {c} ocupada com sucesso.")
else:
    print(f"Não foi possível ocupar a vaga {c}.")
