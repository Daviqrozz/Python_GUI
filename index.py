import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as conn
import csv
from os import path, getcwd

dbpath = path.join(getcwd(), "telefones.sqlite")

janela = tk.Tk()
janela.title("Exportador CSV")
janela.geometry("800x600")
janela.resizable(True, False)

nome, telefone, itens = tk.StringVar(), tk.StringVar(), tk.StringVar()

def inserir():
    with conn.connect(dbpath) as cx:
        query = "insert into contatos (nome, telefone) values (?,?);"
        cursor = cx.cursor()
        cursor.execute(query, (nome.get(), telefone.get()))
        print("Dados inseridos com sucesso")
    ler()

def limpar_tabela():
    try:
        with conn.connect(dbpath) as cx:
            query = "DELETE FROM contatos;"
            cursor = cx.cursor()
            cursor.execute(query)
            messagebox.showinfo("Sucesso", "Tabela limpa com sucesso.")
    except conn.Error as e:
        messagebox.showerror("Erro", f"Erro ao limpar tabela: {e}")
    ler()

def exportar_csv():
    try:
        with conn.connect(dbpath) as cx, open("contatos.csv", "w", newline="") as csv_file:
            query = "SELECT * FROM contatos;"
            cursor = cx.cursor()
            cursor.execute(query)
            writer = csv.writer(csv_file)
            writer.writerow([i[0] for i in cursor.description])  # Escrever cabeçalho
            writer.writerows(cursor.fetchall())  # Escrever os dados
        messagebox.showinfo("Sucesso", "Dados exportados para contatos.csv.")
    except conn.Error as e:
        messagebox.showerror("Erro", f"Erro ao exportar dados: {e}")

def ler():
    with conn.connect(dbpath) as cx:
        query = "select nome from contatos;"
        cursor = cx.cursor()
        cursor.execute(query)
        dados = cursor.fetchall()
        s = ""
        for i in dados:
            s += i[0] + "\n"
        
        itens.set(s)

# inicializacao do componente label
ttk.Label(janela, text="Nome").grid(column=10, row=20)
ttk.Entry(janela, textvariable=nome).grid(column=20, row=20)
ttk.Label(janela, text="Telefone").grid(column=10, row=40)
ttk.Entry(janela, textvariable=telefone).grid(column=20, row=40)
ttk.Button(janela, text="Salvar", command=inserir).grid(column=20, row=60)
ttk.Button(janela, text="Limpar", command=limpar_tabela).grid(column=20, row=80)
tk.Listbox(janela, listvariable=itens).grid(column=20, row=100)
ttk.Button(janela, text="Exportar CSV", command=exportar_csv).grid(column=20, row=120)

janela.mainloop()
