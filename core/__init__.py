import os
import ray
import re
import subprocess
import time
import pandas as pd
import json
from  icmplib  import  ping
from icmplib.exceptions import TimeoutExceeded

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from time import sleep
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

tracert_in = {
        "name" : (), #nome
        "host" : (), #Host
        }

portal_out = {
        "name" : (), #nome
        "host" : (), #Host
        "ipRst": [], #Ip
        "all_pct":[], #Todos os pct
        "time": [], #hora
        "mtr": [] #mtr
        }
dns_out = {
        "name" : (), #nome
        "host" : (), #Host
        "ipRst": [], #Ip
        "all_pct":[], #Todos os pct
        "time": [], #hora
        "mtr": [] #mtr
        }
host_out = {
        "name" : (), #nome
        "host" : (), #Host
        "ipRst": [], #Ip
        "all_pct":[], #Todos os pct
        "time": [], #hora
        "mtr": [] #mtr
        }
gateway_out = {
        "name" : (), #nome
        "host" : (), #Host
        "ipRst": [], #Ip
        "all_pct":[], #Todos os pct
        "time": [], #hora
        "mtr": [] #mtr
        }

"""Variavel global evento seleção de portal"""

"""===FIM VARIAVEIS INTERFACE==="""
ray.init()

@ray.remote
def ptext(txt: str):
    datetime = time.strftime('%H:%M:%S', time.localtime())
    return print(f'\n{datetime}: {txt}')

@ray.remote
def sip_alg(): 
    os.startfile("program\sip-alg-detector.exe")
    return True

@ray.remote
def tracert(name: str, host: str) -> bool:
    """ Esse codigo recebe um nome e um IP, 
    para lançar um tracert via os e retornar 
    o resultado em um dict e retornar True quando finalizado. 
    """
    nm = name
    hst = host
    lls = (f'{nm}_out')
    c=1
    ipv4 = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    txt1 = (f'Rastreando a rota para {hst} com no máximo 30 saltos')
    ptext(txt1)

    try: 
        tracert = subprocess.Popen(
                "tracert /d /h 30 " + hst,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)

        lines = tracert.stdout.readlines()
        res = b''.join(lines).decode("utf-8", "ignore")
        
        result = re.findall(ipv4, res)[1:]

        txt2 = ('Exibindo resultados.')
        ptext(txt2)

        for ip in result:
            #Escrever na tela e add a list
            txt3 = (f'{c} - {ip}')
            ptext(txt3)
            c += 1
            sleep(1)
        
        #Adicionando valores a lista
        txt4 = ('Adicionando valores a lista.')
        ptext(txt4)

        for p in result:
            lls["ipRst"].append(p)
            lls["all_pct"].append([])
            lls["time"].append([])
            lls["mtr"].append([])

        ptext(lls.values)

    except subprocess.TimeoutExpired:
        print('***')
    
    return (True)

def pingMtr(name: str, hst: str, qt_pct: int, id: int) -> bool:
    """ Esse codigo recebe um name, host, quantidade e um numero, 
    execulta 3 solicitações de ICMP no host e retorna os valores,
    o ping se mantem com base na quantidade e o ID é o valor no 
    dict que é localizado pelo nome.
    """
    #VARIAVEIS
    count = qt_pct
    nm = name
    hst = hst
    p = id
    datetime = time.strftime('%H:%M:%S', time.localtime())
    lls = (f'{nm}_out')
    c = 1

    txt1 = (f'Disparando {count} pct para {hst} com 56 bytes de dados:\n')
    ptext(txt1)

    for s in range(count):   
        try:
            # Enviamos o pedido
            request = ping(hst, count=3, privileged=True, id=c )
            #Adicionando valores a biblioteca

            for i in request.rtts:
                lls["all_pct"][id].append(f'{i:.3f}')
                sleep(1)
                lls["time"][id].append(datetime)

            #MANPULANDO SAIDA
            hora = lls["time"][p][-1] #hora
            num = c #Num
            sent = len(lls["all_pct"][p])
            recv = len(lls["all_pct"][p]) #Pct recebidos
            loss = sent%recv #Media perdas ATUALIZAR
            avg = float('{:.3f}'.format(request.avg_rtt)) #Media pct
            best = float('{:.3f}'.format(request.min_rtt)) #Melhor pct
            worst = float('{:.3f}'.format(request.max_rtt)) #Pior pct
            lst_out = lls["all_pct"][p][-1]
            last = lst_out.replace("[]", "")
            jitter = request.jitter #Jitter
            
            # Exibimos algumas informações
            table = [hora ,num, hst, loss, sent, recv, avg, best, worst, last, jitter]
            df2 = pd.DataFrame([table], columns=["Hora", "N", "Host", "Loss%", "Sent", "Recv", "Avg", "Best", "Worst", "Last", "Jitter"])
            print(df2)

            #Adicionando valores a biblioteca
            lls["mtr"][id] = (table)
            c += 1

        except TimeoutExceeded:
            # O tempo limite foi atingido
            txt2 = ('Request timeout for icmp_seq ***')
            ptext(txt2)
        
        txt3 = ('Completo.')
        ptext(txt3)
        
        return (True)

@ray.remote
def createJson(name: str) -> bool:
    """Esse codigo tem que receber um nome
    e gravar o dict em um json, dados esse
    que ele vai localizar usando o nome
    """
    nm = name

    txt1 = ('Gravando arquivos no json.')
    ptext(txt1)

    json_str = json.dumps(f'{nm}_out')

    txt2 = (json_str)
    ptext(txt2)

    with open('log\log_{}.json'.format(nm), 'w') as fh:
        fh.write(f'\n{json_str}')

    txt3 = ('Completo.')
    ptext(txt3)
    
    return (True)

@ray.remote
def matplot(name, saida_y, saida_x, tam_min, tam_max, local):
    #name, saida_y, saida_x, tam_min, tam_max = ping_portal()

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