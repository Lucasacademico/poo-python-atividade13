# classes/funcionario.py
from abc import ABC, abstractmethod

# Classe abstrata Funcionario
class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @abstractmethod
    def calcular_salario(self):
        pass
