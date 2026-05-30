#main
import tkinter as tk
from interface import criar_interface
from login import criar_login


janela = tk.Tk()
janela.title('Sistema de biblioteca')
janela.geometry('500x500')

app_sistema = criar_interface(janela)
app_sistema.pack_forget()
criar_login(janela, app_sistema)

janela.mainloop()