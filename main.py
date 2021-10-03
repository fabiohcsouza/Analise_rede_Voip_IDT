from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as st
import time
import core
import threading

"""TELA PRINCIPAL"""

#Responsável pela tela principal e resoluções padrão.

app = tk.Tk()

app.geometry('980x720+480+170')
app.title('Analise rede VoIP - Net2Phone')
#app.iconbitmap('path/to/images/net2phone.ico')
app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='images/net2phone.png'))
app.resizable(False, False)

lb_top = ttk.Label(app, 
    text=('TROUBLESHOOT VOIP - github.com/fabiohcsouza/Analise_rede_VoIP'),
    background="#00008B",
    foreground="white",
    anchor=CENTER
)
lb_top.place(x=330, y=1)

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

"""FUNÇÕES INTERFACE"""

def op_check1(event): #Essa função armazena os valores var do widget ccb.
    global resp_1, resp_portal
    resp_1 = ccb.get()
    resp_portal = core.portal_entrada[resp_1]
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
        if resp_1 in core.portais and c == "SIM" and resp4 > 0:
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
        threading.Thread(target=core.ping_IP('8.8.8.8',resp4 ,'DNS Google', fra2)).start()
    if num == 4:
        text_area.insert(tk.INSERT, 'Iniciando Sip Alg...\n')
        time.sleep(3)
        threading.Thread(target=core.sip_alg()).start()
    if num == 5:
        text_area.insert(tk.INSERT, 'Iniciando Ping Gateway...\n')
        time.sleep(3)
        threading.Thread(target=core.ping_IP(resp5, resp4, 'GATEWAY', fra3)).start()
    if num == 6:
        text_area.insert(tk.INSERT, 'Iniciando Ping Host...\n')
        time.sleep(3)
        threading.Thread(target=core.ping_IP(resp6, resp4, 'HOST', fra4)).start()

def a1(resp_portal, resp4, resp_1, fra1):
            threading.Thread(target=core.ping_IP(resp_portal, resp4, resp_1, fra1)).start()
    
def pular_l(r1): #Essa função cria uma label
    lv1 = ttk.Label(frame1, text='')
    lv1.grid(row= r1, column=0)

"""INICIO ROW 1"""

ret1 = ttk.Label(frame1, relief='solid') #Linha solida
ret2 = ttk.Label(frame1, relief='solid') #Linha solida


lb1 = ttk.Label(frame1, text=('• Selecione um portal'), justify=LEFT) #Label frase

# Caixa de seleção 
cbb_var = tk.Variable
ccb = ttk.Combobox(frame1, textvariable=cbb_var)
ccb['values'] = core.portais
ccb.bind("<<ComboboxSelected>>", op_check1)

# Label saida Portal
lb2 = ttk.Label(frame1, text=' - Saída portal') 

# Label Gateway
lb4 = ttk.Label(frame1, text="• Informe IP gateway") 

# Entry IP Gateway
len2_var = StringVar
len2 = ttk.Entry(frame1, textvariable=len2_var)

# Label host
lb6 = ttk.Label(frame1, text="- Informe IP host")  

# Entry IP Host 
len3_var = StringVar
len3 = ttk.Entry(frame1, textvariable=len3_var)

ret1.place(x=3 , y=3, height=130, width=550)
#pular_l(0)
lb1.grid(row=1, column=0)
ccb.grid(row=1, column=1)
lb2.grid(row=1, column=2)
pular_l(2)
lb4.grid(row=3, column=0)
len2.grid(row=3, column=1)
lb6.grid(row=3, column=2)
len3.grid(row=3, column=3)
pular_l(4)

# Botão execultar
bt1 = ttk.Button(frame1, text='Execultar', command= lambda: op_check2('SIM'))
bt1.grid(row=5, column=0)

# Botão Parar
bt1 = ttk.Button(frame1, text='Extrair')
bt1.grid(row=5, column=1)

# varBarra=DoubleVar
# pb=ttk.Progressbar(frame1, variable=varBarra, maximum=100)
# pb.place(x=50, y=200, width=300, height=40)

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

nb2.add(fra1, text="MTR-Portal")
nb2.add(fra2, text="MTR-Google")
nb2.add(fra3, text="MTR")
nb2.add(fra4, text="Gateway")

"""FIM NOTEBOOK"""

text_area = st.ScrolledText(fra1)
text_area.place(x=565 , y=10, height=625, width=500)

app.tk.mainloop()