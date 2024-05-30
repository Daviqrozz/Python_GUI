import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as conn
import csv
import re
from os import path, getcwd

dbpath = path.join(getcwd(), "telefones.sqlite")

janela = tk.Tk()
janela.eval("tk::PlaceWindow %s center" % janela.winfo_pathname(janela.winfo_id()))
janela.title("Exportador CSV")
janela.geometry("500x500")
janela.resizable(True, False)

nome, telefone, itens = tk.StringVar(), tk.StringVar(), tk.StringVar()


# Funçao de inserir dados no banco
def inserir():
    nome_val = nome.get()
    telefone_val = telefone.get()
    telefone_padrao = '0'

    #CONDIÇOES DE VALIDAÇAO
    if not nome_val or not telefone_val:
        print("Por favor, preencha todos os campos.")
        messagebox.showinfo("Por favor", "Preencha todos os campos corretamente")
        return
    elif telefone_val != telefone_padrao:
        print("O numero de telefone esta incorreto")
        messagebox.showinfo("Por favor", "Verifique se o numero de telefone esta incorreto")
        return
    try:
        with conn.connect(dbpath) as cx:
            query = "insert into contatos (nome, telefone) values (?,?);"
            cursor = cx.cursor()
            cursor.execute(query, (nome_val, telefone_val))
            cx.commit()
            print("Dados inseridos com sucesso")
            print(f"Nome: {nome_val} - Telefone: {telefone_val}")
    except Exception as e:
        print("Dados não foram inseridos")
        print(f"Erro: {e}")

    ler()


# Funçao de limpar tabela
def limpar_tabela():
    try:
        with conn.connect(dbpath) as cx:
            query = "DELETE FROM contatos;"
            cursor = cx.cursor()
            cursor.execute(query)
            messagebox.showinfo("Sucesso", "Tabela limpa com sucesso.")
            print("Dados limpos com sucesso")
    except conn.Error as e:
        print("Dados limpados com sucesso")
        messagebox.showerror("Erro", f"Erro ao limpar tabela: {e}")
    ler()


# Funçao de exportar dados para arquivo csv
def exportar_csv():
    try:
        with conn.connect(dbpath) as cx, open(
            "contatos.csv", "w", newline=""
        ) as csv_file:
            query = "SELECT * FROM contatos;"
            cursor = cx.cursor()
            cursor.execute(query)
            writer = csv.writer(csv_file)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(cursor.fetchall())
        messagebox.showinfo("Sucesso", "Dados exportados para contatos.csv.")
    except conn.Error as e:
        messagebox.showerror("Erro", f"Erro ao exportar dados: {e}")


# Funçao de retornar os dados tragos da consulta para uma lista formatada
def ler():
    with conn.connect(dbpath) as cx:
        query = "select nome,telefone from contatos;"
        cursor = cx.cursor()
        cursor.execute(query)
        dados = cursor.fetchall()

        lista_itens = [f"{nome} - Telefone:{telefone}" for nome, telefone in dados]

        itens.set(lista_itens)


ler()

ttk.Label(janela, text="Nome").place(x=200, y=40)
ttk.Entry(janela, textvariable=nome).place(x=200, y=60)
ttk.Label(janela, text="Telefone").place(x=200, y=85)
ttk.Entry(janela, textvariable=telefone).place(x=200, y=105)
ttk.Button(janela, text="Salvar", command=inserir).place(x=200, y=135)
ttk.Button(janela, text="Limpar", command=limpar_tabela).place(x=200, y=370)
ttk.Label(janela, text="Lista de contatos").place(x=200, y=180)
tk.Listbox(janela, width=50, listvariable=itens).place(x=100, y=200)
ttk.Button(janela, text="Exportar CSV", command=exportar_csv).place(x=200, y=395)

janela.mainloop()
