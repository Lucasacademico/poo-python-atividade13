# classes/comissionado.py
from classes.funcionario import Funcionario

class Comissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.salario_base = salario_base
        self.vendas = vendas
        self.taxa_comissao = taxa_comissao
    
    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.taxa_comissao / 100)
