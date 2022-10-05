from tkinter import *
import integrarLibeOffice as inlb

class Frames:
	def __init__(self,root):
		self.frame = 0


	def destruir(self):
		self.frame.destroy()
		self.frame = 0

	def construir_tela_abrirOrdem(self,root):
		

		div2 = Frame(self.frame)
		div2.place(x=25,y=100,width=1000,height=300)
		lbl_tag = Label(div2,text='          TAG:                                                           ')
		lbl_tag.grid(row=2,column=0)
		lbl_tipo_do_equipamento = Label(div2,text='        Tipo do equipamento:                                           ')
		lbl_tipo_do_equipamento.grid(row=2,column=2)
		lbl_tipo_do_servico = Label(div2,text='        Tipo do serviço:                                               ')
		lbl_tipo_do_servico.grid(row=2,column=3)
		entry_tg = Entry(div2)
		entry_tg.grid(row=3,column=0)
		entry_tipo_do_equipamento = Entry(div2)
		entry_tipo_do_equipamento.grid(row=3,column=2)
		entry_tipo_do_servico = Entry(div2)
		entry_tipo_do_servico.grid(row=3,column=3)
		Label(div2,text="Descricao do serviço").place(x=50,y=180,width=100,height=20)
		text_descricaoDoServico = Text(div2)
		text_descricaoDoServico.place(x=50,y=200,width=500,height=80)

		div = Frame(self.frame)
		div.place(x=25,y=60,width=300,height=100)
		btn_salvar = Button(div,text='Salvar',command= lambda: inlb.Salvar.salvar_ordem_aberta(entry_tg.get() ,entry_tipo_do_equipamento.get(),entry_tipo_do_servico.get() ,text_descricaoDoServico.get(1.0,END)))
		btn_salvar.grid(row=0,column=0)
		btn_imprimir = Button(div,text='Imprimir')
		btn_imprimir.grid(row=0,column=1)
		btn_cancelar = Button(div,text='Cancelar',command= lambda: self.destruir())
		btn_cancelar.grid(row=0,column=2)


	def construir_tela_editarOrdem(self,root):
		div = Frame(self.frame)
		div.place(x=70,y=70,width=400,height=30)
		ety_numero_da_ordem = Entry(div)
		ety_numero_da_ordem .place(x=0,y=0,width=200,height=30)
		btn_procurar = Button(div,text="Buscar")
		btn_procurar.place(x=250,y=0,width=80,height=30)
		btn_cancelar = Button(div,text="Cancelar",command= lambda: self.destruir())
		btn_cancelar.place(x=340,y=0,width=80,height=30)

	def construir_tela_fecharOrdem(self,root):
		div = Frame(self.frame)
		div.place(x=10,y=20,width=300,height=100)
		btn_fechar = Button(div,text='Fechar Ordem')
		btn_fechar.grid(row=0,column=0)
		btn_imprimir = Button(div,text='Imprimir')
		btn_imprimir.grid(row=0,column=1)
		btn_cancelar = Button(div,text='Cancelar',command= lambda: self.destruir())
		btn_cancelar.grid(row=0,column=2)

		'''div2 = Frame(self.frame)
		div2.place(x=10,y=60,width=1080,height=100)
		lbl_tag = Label(div2,text='          TAG                                                           ')
		lbl_tag.grid(row=0,column=0)
		lbl_tipo_do_equipamento = Label(div2,text='        Tipo do equipamento                                           ')
		lbl_tipo_do_equipamento.grid(row=0,column=2)
		lbl_tipo_do_servico = Label(div2,text='        Tipo do serviço                                               ')
		lbl_tipo_do_servico.grid(row=0,column=3)
		entry_tg = Entry(div2)
		entry_tg.grid(row=1,column=0)
		entry_tipo_do_equipamento = Entry(div2)
		entry_tipo_do_equipamento.grid(row=1,column=2)
		entry_tipo_do_servico = Entry(div2)
		entry_tipo_do_servico.grid(row=1,column=3)'''



	def formato(self,root,titulo):
		if(self.frame == 0):
			self.frame = LabelFrame(root,text=f'  {titulo}  ', borderwidth=3,relief='solid')
			self.frame.place(x=0,y=40 ,width=1100, height=600)
			if(titulo == 'Abrir Ordem'):
				self.construir_tela_abrirOrdem(root)
			elif(titulo == 'Editar Ordem'):
				self.construir_tela_editarOrdem(root)
			elif(titulo == 'Fechar Ordem'):
				self.construir_tela_fecharOrdem(root)
		else:
			self.destruir()

