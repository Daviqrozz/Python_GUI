import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as conn
import csv
from os import path, getcwd

dbpath = path.join(getcwd(), "telefones.sqlite")

janela = tk.Tk()
janela.eval('tk::PlaceWindow %s center' % janela.winfo_pathname(janela.winfo_id()))
janela.title("Exportador CSV")
janela.geometry("500x500")
janela.resizable(True, False)

nome, telefone, itens = tk.StringVar(), tk.StringVar(), tk.StringVar()

def inserir():
    with conn.connect(dbpath) as cx:
        query = "insert into contatos (nome, telefone) values (?,?);"
        cursor = cx.cursor()
        cursor.execute(query, (nome.get(), telefone.get()))
        #Condiçao de se dados nao forem inseridos, retornar erro na interface.
        if conn.Error == True:
            print('Dados nao foram inseridos')
        else:
            print("Dados inserido com sucesso")
            print(f'Nome:{nome.get()} - Telefone:{telefone.get()}')
            

    ler()

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

def exportar_csv():
    try:
        with conn.connect(dbpath) as cx, open("contatos.csv", "w", newline="") as csv_file:
            query = "SELECT * FROM contatos;"
            cursor = cx.cursor()
            cursor.execute(query)
            writer = csv.writer(csv_file)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(cursor.fetchall())
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


        
ttk.Label(janela, text="Nome").place(x=200,y=40)
ttk.Entry(janela, textvariable=nome).place(x=200,y=60)
ttk.Label(janela, text="Telefone").place(x=200,y=85)
ttk.Entry(janela, textvariable=telefone).place(x=200,y=105)
ttk.Button(janela, text="Salvar", command=inserir).place(x=200,y=135)
ttk.Button(janela, text="Limpar", command=limpar_tabela).place(x=200,y=350)
tk.Listbox(janela, listvariable=itens).place(x=200,y=170)
ttk.Button(janela, text="Exportar CSV", command=exportar_csv).place(x=200,y=375)


janela.mainloop()
