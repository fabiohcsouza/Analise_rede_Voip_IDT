
from tkinter import *
from tkinter import ttk
import tkinter as tk
from variaveis import *
from module.ping_portal import ping_portal
from module.ping_dns import ping_dns
from module.tracert import tracert 
from module.sipalg import sip_alg
from functools import partial

app = tk.Tk()

app.geometry('900x600+500+200')
app.title('Analise rede VoIP - Net2Phone')
app.iconbitmap('images/icon/net2phone.ico')

lb_top = ttk.Label(app, 
    text=('TROUBLESHOOT VOIP - github.com/fabiohcsouza/Analise_rede_VoIP'),
    background="#00008B",
    foreground="white",
    anchor=CENTER
)
lb_top.grid(row=0, column=0)

"""Variaveis check, interface"""

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

# resp_1 = ()
# resp_2 = () 
# resp_3 = ()
# resp_4 = ()

def op_check1(event):
    resp_1 = ccb.get()
    resp_portal = portal_entrada[resp_1]
    lb2['text'] = resp_portal

    return resp_1

def op_check2():
    resp1 = valor_check1.get()
    resp_2 = resp1
    resp2 = valor_check2.get()
    resp_3 = resp2
    resp3 = valor_check3.get()
    resp_4 = resp3

    return resp_2, resp_3, resp_4

# p = ()
# t = ()
# d = ()
# s = ()


def resp():
    resp_1 = op_check1(ccb.get())
    resp_2, resp_3, resp_4 = op_check2()

    if resp_1 in portais:
        p = True
        
    
    else:
        p = False
        

    if resp_2 == 1:
        t1 = True
        t = t1
    else:
        t = False
        

    if resp_3 == 1:
        d = True
        
    else:
        d = False
        

    if resp_4 == 1:
        s = True
        
    else:
        s = False
        
    
    return p, t, d, s

def next(str = "bt1S"):

    p, t, d, s = resp()
    resp_1 = op_check1(ccb.get())

    if p and t == True:
        bt1['text'] = 'S-Ping'
        print("Conluido")
    else:
        print(p, t)

    if p and d == True:
        bt1['text'] = 'S-DNS'
        ping_dns()
    else:
        print(p, d)

    if s == True:

        print(s)
    else:
        print(s)

nb = ttk.Notebook(app)
nb.grid(row=1, column=0)

frame1 = ttk.Frame(nb, width=900, height=500)
frame2 = ttk.Frame(nb, width=900, height=500)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

nb.add(frame1, text="Troubleshoot")
nb.add(frame2, text="Multi-Ping")

lb1 = ttk.Label(frame1, text=(' • Selecione um portal '), justify=LEFT)
lb1.grid(row=0, column=0)
#ret1 = ttk.Label(frame1, relief='solid', width=400).grid(row=0, column=0)

cbb_var = tk.Variable
ccb = ttk.Combobox(frame1, textvariable=cbb_var)
ccb['values'] = portais
#ccb['postcommand'] op_check1
ccb.grid(row=0, column=1)
ccb.bind("<<ComboboxSelected>>", op_check1)

lb2 = ttk.Label(frame1, text=' - Saída portal')
lb2.grid(row=0, column=2)

lb3 = ttk.Label(frame1, text=(' • Selecione as opções '), justify=LEFT)
lb3.grid(row=1, column=0)

valor_check1 = IntVar()
check1 = ttk.Checkbutton(frame1, text="TRACERT",
    variable=valor_check1,
    command = op_check2)
check1.grid(row=1, column=1)

valor_check2 = IntVar()
check2 = ttk.Checkbutton(frame1, text="DNS",
    variable=valor_check2,
    command = op_check2)
check2.grid(row=1, column=2)

valor_check3 = IntVar()
check3 = ttk.Checkbutton(frame1, text="SIP ALG",
    variable=valor_check3,
    command = op_check2)
check3.grid(row=1, column=3)

bt1 = ttk.Button(frame1, text='Execultar', command= lambda: next("bt1s"))
bt1.grid(row=3, column=0)


app.tk.mainloop()