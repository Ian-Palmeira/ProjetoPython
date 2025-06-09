import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        temp = float(entrada.get())
        if opcao.get() == "C->F":
            resultado.set(f"{(temp * 9/5) + 32:.1f} °F")
        else:
            resultado.set(f"{(temp - 32) * 5/9:.1f} °C")
    except:
        resultado.set("Erro")

def limpar():
    entrada.delete(0, tk.END)
    resultado.set("")

def fechar ():
    janela.destroy()


janela = tk.Tk()
janela.geometry("250x200")
janela.title("Conversor De Temperatura")

entrada = tk.Entry(janela)
entrada.pack()

opcao = tk.StringVar(value="C->F")
tk.Radiobutton(janela, text="C → F", variable=opcao, value="C->F").pack()
tk.Radiobutton(janela, text="F → C", variable=opcao, value="F->C").pack()

tk.Button(janela, text="Converter",width=25, command=converter).pack()
tk.Button(janela, text="Limpar",width=25, command=limpar).pack()
tk.Button(janela, text="Fechar",width=25, command=fechar).pack(pady=20)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado).pack()

janela.mainloop() 