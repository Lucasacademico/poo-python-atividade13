
import tkinter as tk
from tkinter import messagebox, ttk
from classes.horista import Horista
from classes.mensalista import Mensalista
from classes.comissionado import Comissionado

# Lista para armazenar os funcionários
funcionarios = []

def centralizar_janela(root, width, height):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela // 2) - (width // 2)
    pos_y = (altura_tela // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
    root.resizable(False, False) 

# Função para adicionar funcionário
def adicionar_funcionario():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    tipo_funcionario = tipo_var.get()
    
    if nome and matricula:
        try:
            if tipo_funcionario == "Horista":
                horas_trabalhadas = float(entry_horas_trabalhadas.get())
                valor_hora = float(entry_valor_hora.get())
                funcionario = Horista(nome, matricula, horas_trabalhadas, valor_hora)
            elif tipo_funcionario == "Mensalista":
                salario_mensal = float(entry_salario_mensal.get())
                funcionario = Mensalista(nome, matricula, salario_mensal)
            elif tipo_funcionario == "Comissionado":
                salario_base = float(entry_salario_base.get())
                vendas = float(entry_vendas.get())
                taxa_comissao = float(entry_taxa_comissao.get())
                funcionario = Comissionado(nome, matricula, salario_base, vendas, taxa_comissao)
            else:
                messagebox.showerror("Erro", "Selecione o tipo de funcionário.")
                return
            
            funcionarios.append(funcionario)
            messagebox.showinfo("Sucesso", f"Funcionário '{funcionario.nome}' adicionado como {tipo_funcionario}!")

            # Atualiza a Treeview com o novo funcionário
            tree.insert("", "end", values=(
                funcionario.nome,
                funcionario.matricula,
                tipo_funcionario,
                funcionario.calcular_salario()
            ))

            # Limpa os campos de entrada
            limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Preencha corretamente os campos numéricos.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")

# Função para calcular o pagamento de todos os funcionários
def calcular_pagamento():
    if funcionarios:
        resultados = []
        for funcionario in funcionarios:
            salario = funcionario.calcular_salario()
            resultados.append(f"{funcionario.nome}: R${salario:.2f}")
        messagebox.showinfo("Pagamentos Calculados", "\n".join(resultados))
    else:
        messagebox.showerror("Erro", "Nenhum funcionário adicionado.")

# Função para atualizar os campos visíveis com base no tipo de funcionário
def atualizar_campos():
    tipo_funcionario = tipo_var.get()
    # Oculta todos os campos específicos
    for widget in campos_especificos.values():
        widget.grid_remove()
    # Exibe apenas os campos específicos para o tipo selecionado
    if tipo_funcionario == "Horista":
        campos_especificos["horas_trabalhadas"].grid(row=3, column=0)
        campos_especificos["valor_hora"].grid(row=4, column=0)
    elif tipo_funcionario == "Mensalista":
        campos_especificos["salario_mensal"].grid(row=5, column=0)
    elif tipo_funcionario == "Comissionado":
        campos_especificos["salario_base"].grid(row=6, column=0)
        campos_especificos["vendas"].grid(row=7, column=0)
        campos_especificos["taxa_comissao"].grid(row=8, column=0)

# Função para limpar campos após adicionar funcionário
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_matricula.delete(0, tk.END)
    for widget in campos_especificos.values():
        widget.entry.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Pagamento de Funcionários")
centralizar_janela(root, 800, 600)
# root.state('zoomed')  # Para maximizar a janela

# Campos de entrada
tk.Label(root, text="Nome do Funcionário:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Matrícula:").grid(row=1, column=0)
entry_matricula = tk.Entry(root)
entry_matricula.grid(row=1, column=1)

# Tipo de funcionário
tk.Label(root, text="Tipo de Funcionário:").grid(row=2, column=0)
tipo_var = tk.StringVar()
tipo_menu = ttk.Combobox(root, textvariable=tipo_var, values=["Horista", "Mensalista", "Comissionado"])
tipo_menu.grid(row=2, column=1)
tipo_menu.bind("<<ComboboxSelected>>", lambda e: atualizar_campos())

# Campos específicos por tipo de funcionário
campos_especificos = {
    "horas_trabalhadas": tk.Label(root, text="Horas Trabalhadas:"),
    "valor_hora": tk.Label(root, text="Valor Hora:"),
    "salario_mensal": tk.Label(root, text="Salário Mensal:"),
    "salario_base": tk.Label(root, text="Salário Base:"),
    "vendas": tk.Label(root, text="Vendas:"),
    "taxa_comissao": tk.Label(root, text="Taxa Comissão (%):")
}

# Entradas específicas
entry_horas_trabalhadas = tk.Entry(root)
entry_valor_hora = tk.Entry(root)
entry_salario_mensal = tk.Entry(root)
entry_salario_base = tk.Entry(root)
entry_vendas = tk.Entry(root)
entry_taxa_comissao = tk.Entry(root)

# Associar entradas aos labels no dicionário
campos_especificos["horas_trabalhadas"].entry = entry_horas_trabalhadas
campos_especificos["valor_hora"].entry = entry_valor_hora
campos_especificos["salario_mensal"].entry = entry_salario_mensal
campos_especificos["salario_base"].entry = entry_salario_base
campos_especificos["vendas"].entry = entry_vendas
campos_especificos["taxa_comissao"].entry = entry_taxa_comissao

# Posicionamento inicial
for i, (label, entry) in enumerate(campos_especificos.items(), start=3):
    entry.entry.grid(row=i, column=1)

# Botões
btn_adicionar = tk.Button(root, text="Adicionar Funcionário", command=adicionar_funcionario)
btn_adicionar.grid(row=9, column=0)

btn_calcular = tk.Button(root, text="Calcular Pagamentos", command=calcular_pagamento)
btn_calcular.grid(row=9, column=1)

# Configuração da Treeview
columns = ("Nome", "Matrícula", "Tipo", "Salário")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Centraliza o texto nas colunas
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.grid(row=10, column=0, columnspan=2)

# Iniciar a interface
root.mainloop()
