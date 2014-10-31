 ("Entre com o valor # 2")
from tkinter import *

def principal():
	# definição da janela
	janela = Tk()

	# definindo o título da janela
	janela.title("Exemplo #1")
	
	# componentes
	botão1 = Button(janela, bg="red", fg="white", text = "Botão #1")
	botão2 = Button(janela, bg="blue", fg="yellow", text = "Botão #2" )
	

	# organização na tela
	botão1.pack()
	botão2.pack()
	
	# definindo "ações" para os botões
	botão1.configure(command=click_botão1)
	botão2.configure(command=click_botão2)

# ações
def click_botão1():
	print("evento: click no botão 1")

def click_botão2():
	print("evento: click no botão 2")

# rodando nosso programa
if __name__ == '__main__':
	principal()
      
