import openpyxl as opx


caminho = '/home/carlos_abp/Documentos/documentos/manipular.xlsx'

class  Salvar:
    def __init__(self):
        pass
     
    def salvar_ordem_aberta(a,b,c,d):   
        livro = opx.load_workbook(caminho)

        planilha = livro.active

        planilha['A1'] = a
        planilha['B1'] = b
        planilha['C1'] = c
        planilha['D1'] = d
        '''planilha = livro.worksheets.index(0)
        planilha['A1,B1,C1,D1'] = a,b,c,d
'''


        livro.save(caminho)
