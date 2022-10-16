from xml.sax.handler import property_dom_node
from tkinter import *
import tkinter
from datetime import datetime

import pyglet #biblioteca que permite adicionar fonte para o tkinter 
pyglet.font.add_file("digital-7.ttf") #fonte do relógio 


#####cores####

cor1 = "#3d3d3d" #preto
cor2 = "#fafcff" #branca
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelha
cor5 = "#dedcdc" #cinza
cor6 = "#3080f0" #azul 

fundo = cor1
cor = cor6

janela = Tk()
janela.title('Relogio') #title
janela.geometry('440x180') #tamanhoxaltura
janela.resizable(width=FALSE, height=FALSE) #resizable = Não permite alterar o tamanho da janela principal;
janela.configure(bg=cor1) #fundodajanela

def relogio(): #função 
    tempo = datetime.now() #horadocomputador

    hora = tempo.strftime("%H:%M:%S") #hora/minutos/segundo
    dia_semana = tempo.strftime("%A") #semana
    dia = tempo.day #dia da semana 
    mes = tempo.strftime("%b") #mês %b = nome incompleto do mês / %B = nome completo do mês
    ano = tempo.strftime("%Y") #ano
    
    l1.config(text=hora)
    l1.after(200, relogio) #depois de 200 milesimos irá rodar a aplicação
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="10:50:22", font=("digital-7 100"), bg = fundo, fg = cor) # FONTE, FUNDO, COR 
l1.grid(row=0, column = 0, sticky = NW, padx = 5) #POSIÇÃO row = posição

l2 = Label(janela, text="10:50:22", font=("digital-7 17"), bg = fundo, fg = cor) # FONTE, FUNDO, COR 
l2.grid(row=1, column = 0, sticky = NW, padx = 5) #POSIÇÃO 

relogio() #executando função
janela.mainloop() #executando a janela

