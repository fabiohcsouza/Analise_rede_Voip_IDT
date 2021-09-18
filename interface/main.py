
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



def op_check1(event):
    resp = ccb.get()
    resp_portal = portal_entrada[resp]
    lb2['text'] = resp_portal
    resp1 = valor_check1.get()
    resp2 = valor_check2.get()
    resp3 = valor_check3.get()

    if resp in portais:
        p = True
    else:
        p = False
    
    if resp1 == 1:
        t = True
    else:
        t = False

    if resp2 == 1:
        d = True
    else:
        d = False

    if resp3 == 1:
        s = True
    else:
        s = False

    
        if p and t == True:
            
            ping_portal(resp_portal)
            tracert(resp_portal)
        else:
            print('Error')

        if p and d == True:
            
            ping_dns()
        else:
            print('Error')

        if s == True:

            sip_alg()
        else:
            print('Error')


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
    command = op_check1)
check1.grid(row=1, column=1)

valor_check2 = IntVar()
check2 = ttk.Checkbutton(frame1, text="DNS",
    variable=valor_check2,
    command = op_check1)
check2.grid(row=1, column=2)

valor_check3 = IntVar()
check3 = ttk.Checkbutton(frame1, text="SIP ALG",
    variable=valor_check3,
    command = op_check1)
check3.grid(row=1, column=3)

bt1 = ttk.Button(frame1, text='Execultar')
bt1.grid(row=3, column=0)
bt1['command']


app.tk.mainloop()