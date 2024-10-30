# classes/horista.py
from classes.funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    
    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora
