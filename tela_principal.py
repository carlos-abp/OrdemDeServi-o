from tkinter import *
import minitelas as mt
import openpyxl as opx



janela_principal = Tk()


janela_principal.title('Ordem De Serviço')
#centrar janela
## pegar tamanho da tela pelo sistema
tam_x = str(int(janela_principal.winfo_screenwidth()/2)-550)
tam_y = str(int(janela_principal.winfo_screenheight()/2)-325)

##gerar o geometry
centrar = '1100x650+'+tam_x+'+'+tam_y
janela_principal.geometry(centrar)
janela_principal.resizable(False,False)

frames = mt.Frames(janela_principal)

btn_abrir_ordem = Button(janela_principal,text='Abrir Ordem',command = lambda: frames.formato(janela_principal,'Abrir Ordem'))
btn_abrir_ordem.grid(row=0,column=0)
btn_editar_ordem = Button(janela_principal,text='Editar Ordem',command = lambda: frames.formato(janela_principal,'Editar Ordem'))
btn_editar_ordem.grid(row=0,column=1)
btn_fechar_ordem = Button(janela_principal,text='Fechar Ordem',command= lambda: frames.formato(janela_principal,'Fechar Ordem'))
btn_fechar_ordem.grid(row=0,column=2)

div = Frame(janela_principal,background='#aaa',relief='raised',borderwidth=1)
div.place(x=350,y=0,width=900,height=30)
Label(div,text='Cadastros: ',bg='#aaa').place(x=2,y=3,width=90,height=23)


janela_principal.mainloop()