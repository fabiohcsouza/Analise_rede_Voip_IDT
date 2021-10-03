
from time import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as st
import time
import threading

"""FUNÇÕES DO SISTEMA"""
from  icmplib  import  ping
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def sip_alg():
    os.startfile("program\sip-alg-detector.exe")

def ping_IP(IP, tm, name, local_a):
    
    #VARIAVEIS
    address_portal = IP
    interval_qt = 0.2
    nome = name
    local = local_a

    #SISTEMA
    host1 = ping(address_portal, count=tm, interval=interval_qt)

    #MANPULANDO SAIDA
    valor1 = host1.rtts
    max = host1.max_rtt
    min = host1.min_rtt
    
    d = int('{:.0f}'.format(max+5))
    e = int('{:.0f}'.format(min-5))

    #AJUSTANDO SAIDA PARA USO NO MATPLOTLIB
    saida_y = []
    for ms in valor1:
        saida_y.append(int('{:.0f}'.format(ms)))

    saida_x = []
    tam_s = len(saida_y)
    x2 = tam_s + 1
    xx = range(1, x2)
    for n in xx:
        saida_x.append(n)

    #COLOCANDO SAINDO SISTEMA NO LABLE DE TEXTO
    text_area.insert(tk.INSERT, host1)
    
    #INICIANDO MATPLOT COM DADOS DA SAIDA
    
    threading.Thread(target=matplot(name, saida_y, saida_x, e, d, local)).start()


def matplot(name, saida_y, saida_x, tam_min, tam_max, local):
    #name, saida_y, saida_x, tam_min, tam_max = ping_portal()

    text_area.insert(tk.INSERT, 'Montando dados...\n')

    #VARIAVEIS
    nome = name
    y = saida_y
    x = saida_x
    tamMin = tam_min
    tamMax = tam_max
    are = local
    figura = plt.figure(figsize=(8, 4), dpi=60)
    a = figura.add_subplot(111)

    #add x and y labels 
    plt.xlabel('Tempo/Quantidade')
    plt.ylabel('Tempo/ms')

    #Axes range
    plt.axis(ymin=tamMin,ymax=tamMax)

    #add title
    plt.title('Relatorio PING')
    #plot
    #grafico.plot(x, y, label=nome, marker='o')
    a.bar(x, y, label=nome)
    a.legend()

    canva = FigureCanvasTkAgg(figura, are)
    canva.get_tk_widget().place(x=1 , y=1, height=375, width=540)
    canva.draw()

    
    # grafico.show()

"""TELA PRINCIPAL"""

#Responsável pela tela principal e resoluções padrão.

app = tk.Tk()

app.geometry('1100x720+480+170')
app.title('Analise rede VoIP - Net2Phone')
#app.iconbitmap('path/to/interface/images/icon/net2phone.ico')
app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='images/icon/net2phone.png'))
app.resizable(False, False)

lb_top = ttk.Label(app, 
    text=('TROUBLESHOOT VOIP - github.com/fabiohcsouza/Analise_rede_VoIP'),
    background="#00008B",
    foreground="white",
    anchor=CENTER
)
lb_top.place(x=330, y=1)

"""FIM TELA PRINCIAL"""



"""INICIO NOTEBOOK"""

# Especificações notebook. 

nb = ttk.Notebook(app)
nb.place(x=5, y=20, height=685, width=1090)

frame1 = ttk.Frame(nb, width=980, height=600)
frame2 = ttk.Frame(nb, width=980, height=600)
frame3 = ttk.Frame(nb, width=980, height=600)
frame4 = ttk.Frame(nb, width=980, height=600)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

nb.add(frame1, text="Troubleshoot")
nb.add(frame2, text="Multi-Ping")
nb.add(frame3, text="Nmap")
nb.add(frame4, text="Dados")

"""INICIO NOTEBOOK 2"""

nb2 = ttk.Notebook(frame1)
nb2.place(x=10 , y=215, height=420, width=542)

fra1 = ttk.Frame(nb2, width=380, height=550)
fra2 = ttk.Frame(nb2, width=380, height=550)
fra3 = ttk.Frame(nb2, width=380, height=550)
fra4 = ttk.Frame(nb2, width=380, height=550)

fra1.pack(fill='both', expand=True)
fra2.pack(fill='both', expand=True)
fra3.pack(fill='both', expand=True)
fra4.pack(fill='both', expand=True)

nb2.add(fra1, text="Portal")
nb2.add(fra2, text="DNS")
nb2.add(fra3, text="Host")
nb2.add(fra4, text="Gateway")


"""FIM NOTEBOOK"""


"""===VARIAVEIS INTERFACE==="""

"""Dicionario de portais com proxy para uso:"""
portal_entrada = {
        "Portal 1": "proxy.idtbrasilhosted.com",
        "Portal 2": "proxy2.idtbrasilhosted.com",
        "Portal 3": "proxy3.idtbrasilhosted.com",
        "Portal 4": "proxy4.idtbrasilhosted.com",
        "Portal 5": "proxy5.idtbrasilhosted.com",
        "Portal 6": "proxy6.idtbrasilhosted.com",
        "Portal 7": "proxy7.idtbrasilhosted.com",
        "Portal 8": "proxy8.idtbrasilhosted.com",
        "Portal 9": "proxy9.idtbrasilhosted.com",
        "Portal 10": "proxy10.idtbrasilhosted.com",
        "Portal 11": "proxy11.idtbrasilhosted.com",
        "Portal 12": "proxy12.idtbrasilhosted.com",
    }

"""Variaveis combobox"""
portais = (["Portal 1", "Portal 2", "Portal 3", "Portal 4", "Portal 5", "Portal 6", 
                "Portal 7", "Portal 8", "Portal 9", "Portal 10", "Portal 11", "Portal 12"])

"""Variavel global evento seleção de portal"""

"""===FIM VARIAVEIS INTERFACE==="""

"""FUNÇÕES INTERFACE"""

def op_check1(event): #Essa função armazena os valores var do widget ccb.
    global resp_1, resp_portal
    resp_1 = ccb.get()
    resp_portal = portal_entrada[resp_1]
    lb2['text'] = "-", resp_portal

    return resp_1, resp_portal

def op_check2(c): #Essa função armazena os valores var do widget checkbox
    resp1 = valor_check1.get()
    resp2 = valor_check2.get()
    resp4 = int(len1.get())
    resp3 = valor_check3.get()
    resp5 = bool(len2.get())
    resp6 = bool(len3.get())
    

        #PING PORTAL
    try:
        if resp_1 in portais and c == "SIM" and resp4 > 0:
            next(1)
    except:
        pass
    try:
        #TRACERT
        if resp1 ==1 and c == "SIM":
            next(2)
    except:
        pass
    try:
        #DNS
        if resp2 == 1 and c == "SIM"  and resp4 > 0:
            next(3) 
    except:
        pass
    try:
        #SIP ALG
        if resp3 == 1 and c == "SIM":
            next(4)
    except:
        pass
    try:
        #PING IP GATEWAY
        if resp5 == True and c == "SIM"  and resp4 > 0:
            next(5)
    except:
        pass
    try:
        #PING IP HOST
        if resp6 == True and c == "SIM" and resp4 > 0:
            next(6)
    except:
        pass
    
def next(num: int): #Essa função execulta os comando, vinculada ao botao execultar. 
    resp_1 = ccb.get()
    resp4 = int(len1.get())
    resp5 = len2.get()
    resp6 = len3.get()

    if num == 1: 
        text_area.insert(tk.INSERT, 'Iniciando Ping Portal... \n'), app.update, time.sleep(3)
        a1(resp_portal, resp4, resp_1, fra1)
        
    if num == 2:
        text_area.insert(tk.INSERT, 'Iniciando Tracert para portal...\n')
        time.sleep(3)
        print('tracert não pronto')
    if num == 3:
        text_area.insert(tk.INSERT, 'Iniciando Ping DNS Google...\n')
        time.sleep(3)
        threading.Thread(target=ping_IP('8.8.8.8',resp4 ,'DNS Google', fra2)).start()
    if num == 4:
        text_area.insert(tk.INSERT, 'Iniciando Sip Alg...\n')
        time.sleep(3)
        threading.Thread(target=sip_alg()).start()
    if num == 5:
        text_area.insert(tk.INSERT, 'Iniciando Ping Gateway...\n')
        time.sleep(3)
        threading.Thread(target=ping_IP(resp5, resp4, 'GATEWAY', fra3)).start()
    if num == 6:
        text_area.insert(tk.INSERT, 'Iniciando Ping Host...\n')
        time.sleep(3)
        threading.Thread(target=ping_IP(resp6, resp4, 'HOST', fra4)).start()

def a1(resp_portal, resp4, resp_1, fra1):
            threading.Thread(target=ping_IP(resp_portal, resp4, resp_1, fra1)).start()
    
def pular_l(r1, c0): #Essa função cria uma label
    lv1 = ttk.Label(frame1)
    lv1.grid(row= r1, column= c0)

"""INICIO ROW 1"""
pular_l(0, 0)

ret1 = ttk.Label(frame1, relief='solid')

lb1 = ttk.Label(frame1, text=('• Selecione um portal'), justify=LEFT)

text_area = st.ScrolledText(frame1)

cbb_var = tk.Variable
ccb = ttk.Combobox(frame1, textvariable=cbb_var)
ccb['values'] = portais
ccb.bind("<<ComboboxSelected>>", op_check1)

lb2 = ttk.Label(frame1, text=' - Saída portal')

text_area.place(x=565 , y=10, height=625, width=500)
ret1.place(x=10 , y=10, height=200, width=540)
lb1.grid(row=1, column=0)
ccb.grid(row=1, column=1)
lb2.grid(row=1, column=2)

"""FIM ROW 1"""

"""INICIO ROW 3"""

pular_l(2,0)

lb9 = ttk.Label(frame1, text=('• Tempo de execução'), justify=LEFT)
len1_var = tk.IntVar
len1 = ttk.Entry(frame1, textvariable=len1_var)
lb10 = ttk.Label(frame1, text=('Ex. 6000 = 1 hora'))

lb9.grid(row=3, column=0)
len1.grid(row=3, column=1)
lb10.grid(row=3, column=2)

"""INICIO ROW 5"""

pular_l(4,0)

lb3 = ttk.Label(frame1, text=('• Selecione as opções'), justify=LEFT)

valor_check1 = IntVar()
check1 = ttk.Checkbutton(frame1, text="TRACERT",
    variable=valor_check1)

valor_check2 = IntVar()
check2 = ttk.Checkbutton(frame1, text="DNS",
    variable=valor_check2)

valor_check3 = IntVar()
check3 = ttk.Checkbutton(frame1, text="SIP ALG",
    variable=valor_check3)

lb3.grid(row=5, column=0)
check1.grid(row=5, column=1)
check2.grid(row=5, column=2)
check3.grid(row=5, column=3)

"""FIM ROW 5"""

"""INICIO ROW 7"""

pular_l(6,0)

lb4 = ttk.Label(frame1, text="• Informe IP gateway")

len2_var = StringVar
len2 = ttk.Entry(frame1, textvariable=len2_var)

lb6 = ttk.Label(frame1, text="- Informe IP host")

len3_var = StringVar
len3 = ttk.Entry(frame1, textvariable=len3_var)

lb4.grid(row=7, column=0)
len2.grid(row=7, column=1)
lb6.grid(row=7, column=2)
len3.grid(row=7, column=3)

"""FIM ROW 7"""

"""INICIO ROW 9"""
pular_l(8, 0)
bt1 = ttk.Button(frame1, text='Execultar', command= lambda: op_check2('SIM'))
bt1.grid(row=9, column=0)

bt1 = ttk.Button(frame1, text='Extrair')
bt1.grid(row=9, column=1)

# varBarra=DoubleVar
# pb=ttk.Progressbar(frame1, variable=varBarra, maximum=100)
# pb.place(x=50, y=200, width=300, height=40)

"""FIM ROW 9"""

app.tk.mainloop()