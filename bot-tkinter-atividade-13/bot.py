from botcity.core import DesktopBot
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False
import interface
import time
import threading

import subprocess

from classes.horista import Horista
from classes.comissionado import Comissionado
from classes.mensalista import Mensalista

# def run_interface():
#     app_path = r"C:\Users\matutino\Desktop\entrega\bot-tkinter-atividade-13\interface.py"
#     subprocess.Popen(["python", app_path]) 

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    funcionarios = []

    funcionario1 = Horista("Carlos Silva", "001", 20.0, 160)  # Exemplo de Horista
    funcionarios.append(funcionario1)

    funcionario2 = Comissionado("Ana Costa", "002", 3000.0, 0.1, 5000.0)  # Exemplo de Comissionado
    funcionarios.append(funcionario2)

    funcionario3 = Mensalista("Pedro Santos", "003", 3000.0)  # Exemplo de Mensalista
    funcionarios.append(funcionario3)

    funcionario4 = Horista("Jubileu Silva", "004", 25.0, 180)  # Exemplo de Mensalista
    funcionarios.append(funcionario4)

    for funcionario in funcionarios:
        if isinstance(funcionario, Horista):
            print(f"Horista criado: {funcionario.nome}, Matrícula: {funcionario.matricula}, Salário: R$ {funcionario.calcular_salario()}")
        elif isinstance(funcionario, Comissionado):
            print(f"Comissionado criado: {funcionario.nome}, Matrícula: {funcionario.matricula}, Salário: R$ {funcionario.calcular_salario()}")
        elif isinstance(funcionario, Mensalista):
            print(f"Mensalista criado: {funcionario.nome}, Matrícula: {funcionario.matricula}, Salário: R$ {funcionario.calcular_salario()}")

    # threading.Thread(target=run_interface).start()
    app_path = r"C:\Users\matutino\Desktop\entrega\bot-tkinter-atividade-13\interface.py"
    subprocess.Popen(["python", app_path]) 

    for funcionario in funcionarios:
        if not bot.find("campo_nome", matching=0.97, waiting_time=10000):
            not_found("campo_nome")
        bot.click_relative(434, 7)
        bot.paste(f'{funcionario.nome}') 
        
        if not bot.find("campo_matricula", matching=0.97, waiting_time=10000):
            not_found("campo_matricula")
        bot.click_relative(389, 5)
        bot.paste(f'{funcionario.matricula}')  

        if not bot.find("campo_tipo_funcionario", matching=0.97, waiting_time=10000):
            not_found("campo_tipo_funcionario")
        bot.click_relative(482, 6)
        bot.control_a()
        bot.backspace()

        if isinstance(funcionario, Horista):
            if not bot.find("select_dropdown", matching=0.97, waiting_time=10000):
                not_found("select_dropdown")
            bot.click()
            bot.enter()

            if not bot.find("campo_horas_trabalhadas", matching=0.97, waiting_time=10000):
                not_found("campo_horas_trabalhadas")
            bot.click_relative(414, 9)
            bot.paste(f'{funcionario.horas_trabalhadas}')  

            if not bot.find("campo_valor_hora", matching=0.97, waiting_time=10000):
                not_found("campo_valor_hora")
            bot.click_relative(406, 7)
            bot.paste(f'{funcionario.valor_hora}')

            if not bot.find("btn-cadastrar", matching=0.97, waiting_time=10000):
                not_found("btn-cadastrar")
            bot.click()
            bot.enter()
            
        elif isinstance(funcionario, Comissionado):
            if not bot.find("select_dropdown", matching=0.97, waiting_time=10000):
                not_found("select_dropdown")
            bot.click()
            bot.type_down()
            bot.type_down()
            bot.enter()

            if not bot.find("campo_salario_base", matching=0.97, waiting_time=10000):
                not_found("campo_salario_base")
            bot.click_relative(396, 6)
            bot.paste(f'{funcionario.salario_base}')
            
            if not bot.find("campo_vendas", matching=0.97, waiting_time=10000):
                not_found("campo_vendas")
            bot.click_relative(388, 4)
            bot.paste(f'{funcionario.vendas}')

            if not bot.find("campo_comissao", matching=0.97, waiting_time=10000):
                not_found("campo_comissao")
            bot.click_relative(430, 8)
            bot.paste(f'{funcionario.taxa_comissao}')

            if not bot.find("btn-cadastrar", matching=0.97, waiting_time=10000):
                not_found("btn-cadastrar")
            bot.click()
            bot.enter()

        elif isinstance(funcionario, Mensalista):
            if not bot.find("select_dropdown", matching=0.97, waiting_time=10000):
                not_found("select_dropdown")
            bot.click()
            bot.type_down()
            bot.enter()

            if not bot.find("campo_salario_mensal", matching=0.97, waiting_time=10000):
                not_found("campo_salario_mensal")
            bot.click_relative(409, 10)
            bot.paste(f'{funcionario.salario_mensal}')

            if not bot.find("btn-cadastrar", matching=0.97, waiting_time=10000):
                not_found("btn-cadastrar")
            bot.click()
            bot.enter()

        else:
            print(f"Funcionario Inexistente")
            
    if not bot.find("Calcular_pagamento", matching=0.97, waiting_time=10000):
        not_found("Calcular_pagamento")
    bot.click()
    bot.wait(2000)
    bot.enter()
    bot.alt_f4()
     

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
