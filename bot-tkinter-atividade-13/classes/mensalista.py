# classes/mensalista.py
from classes.funcionario import Funcionario

class Mensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.salario_mensal = salario_mensal
    
    def calcular_salario(self):
        return self.salario_mensal
