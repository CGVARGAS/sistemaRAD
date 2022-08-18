"""
Janela: Trata-se do formulário onde os demais componentes são organizados. No caso da implementação
do sistema, esse componente foi usado da seguinte maneira: janela=tk.Tk()
Rótulo: Que é usado para textos estáticos. No caso do sistema, foi usado para os textos “Nome do Aluno”,
“Nota 1” e “Nota 2”. Para referenciá-los no código, é necessário escrever: tk.Label(janela, text='Texto estático').
Caixa de texto: São usadas para os usuários entrarem com os dados dos alunos. No caso do sistema,
foi usado para entrar com o “nome do aluno”, a “nota 1” e a “nota 2”. Para referenciá-los no código,
é necessário escrever: tk.Entry().
Botão: Usado para iniciar uma ação. No caso do sistema, foi aplicado para cadastrar os dados dos alunos,
calcular suas respectivas médias e determinar situação escolar em que o aluno se encontra. Para
referenciá-los no código, é necessário escrever: tk.Button();
Visão de árvore: bastante útil para visualizar os dados. No sistema, foi usado para uma visualização em
grade dos dados dos alunos, suas médias e respectivas situações. Para referenciá-lo no código,
é necessário escrever: ttk.Treeview().
Barra de rolagem: É um componente útil para interagir com a tabela da “visão de grade”,
quando a quantidade de linhas de registros ultrapassa o limite inicial. Para usar no código,
é necessário escrever ttk.Scrollbar().
A interface gráfica auxilia no entendimento do sistema. Certamente, é mais fácil fazer
sugestões de melhorias a partir de uma experiência real com o sistema do que em um nível abstrato.

"""
import tkinter as tk
from tkinter import ttk
import pandas as pd


janela = tk.Tk()
janela.title('Bem Vindo ao RAD')
janela.geometry('820x600+10+10')
tk.Label(janela, text='Nome do aluno ')
tk.Label(janela, text='Nota Simulado ')
tk.Label(janela, text='Nota AV ')
tk.Entry()
tk.Button()
ttk.Treeview()
ttk.Scrollbar()
janela.mainloop()
