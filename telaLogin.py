from tkinter import *

janela = Tk()
janela.title("Janela nova")
janela.geometry("350x150")
janela.configure(background="#aaa")

lblUsuario = Label(janela, text="Usuário :", background='#aaa')
lblUsuario.place(x=20, y="10", width=100, height=15)

txfUsuario = Entry(janela)
txfUsuario.place(x=100, y=8, width=100, height=20)


lblSenha = Label(janela, text="Senha :", background='#aaa')
lblSenha.place(x=20, y="40", width=100, height=15)

txfSenha = Entry(janela)
txfSenha.place(x=100, y=38, width=100, height=20)

btnAcessar = Button(janela,text="Acessar")
btnAcessar.place(x=250, y=80, width=100, height=20)


janela.mainloop()






