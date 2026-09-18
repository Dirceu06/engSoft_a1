#requisitos a ser implementados
# - (usuário) deve ser simples de usar
# - (usuário) deve mostrar quais vagas disponíveis no estacionamento em tempo real (15 min)
# - (usuário) deve impedir ocupação de vagas que requerem autorização (10 min)
# - IA foi utilizado para implentação da classe e arrumar algumas funções 

import estacionamento
from estacionamento import vagas

vagas_class = estacionamento.Estacionamento()

print("vagas: ", vagas(vagas_class), "\nVagas ocupadas: ", vagas_class.vagas_ocupadas, "\nvagas autorizadas: ", list(vagas_class.vagas_autorizadas))  # Mostrar vagas disponíveis
c = input("Digite o número da vaga que deseja ocupar: ")
c = int(c)


# tem autorização para ocupar a vaga?
# print(c, list(vagas_class.vagas_autorizadas))
autorizado = False
if c in list(vagas_class.vagas_autorizadas): 
    r = input("Você tem autorização para ocupar a vaga? (s/n): ")
    autorizado = r.lower() == 's'



# tentando ocupar a vaga
# estacionamento.ocupar_vaga(vagas_class, c, autorizado)
if vagas_class.ocupar_vaga(c, autorizado):
    print(f"Vaga {c} ocupada com sucesso.")
else:
    print(f"Não foi possível ocupar a vaga {c}.")
