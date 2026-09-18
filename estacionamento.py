# trazer infos do estacionamento
# classe estacionamento
#

class Estacionamento:
    def __init__(self):
        self.vagas_disponiveis = [0, 1, 2, 3, 4, 5] 
        self.vagas_ocupadas = [6, 7, 8, 9, 10]
        self.vagas_autorizadas = [11, 12, 13]  # Vagas que requerem autorização

    def vagas_disponiveis(self):
        return (self.vagas_disponiveis + self.vagas_autorizadas + self.vagas_ocupadas)

    def ocupar_vaga(self, vaga, autorizado=False):
        if not autorizado and vaga in self.vagas_autorizadas:
            return False
        if vaga in self.vagas_disponiveis:
            self.vagas_disponiveis.remove(vaga)
            self.vagas_ocupadas.append(vaga)
            return True
        return False


def vagas(estacionamento):
    return estacionamento.vagas_disponiveis
    
    
