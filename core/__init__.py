import os
import time
from  icmplib  import  ping, multiping , traceroute , resolve
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import threading
from module import *


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

def tracert():
    hops = traceroute("proxy2.idtbrasilhosted.com")

    # saida(hops)

    print(hops)

    print('Distance/TTL    Address    Average round-trip time')

    last_distance = 0

    for hop in hops:
        if last_distance + 1 != hop.distance:
            print('Some gateways are not responding')

    # See the Hop class for details
        print(f'{hop.distance}    {hop.address}    {hop.avg_rtt} ms')

        last_distance = hop.distance



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