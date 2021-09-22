"""FUNÇÕES SISTEMA"""

from  icmplib  import  ping
import matplotlib.pyplot as grafico
import numpy as np


def ping_IP(IP, tm, name):
    
    #VARIAVEIS
    address_portal = IP
    interval_qt = 0.1
    nome = name

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

    arquivo = open('/log/ping_portal.log')
    for item in saida_y:
        


    #COLOCANDO SAINDO SISTEMA NO LABLE DE TEXTO
    #text_area.insert(tk.INSERT, host1)
    
    #INICIANDO MATPLOT COM DADOS DA SAIDA
    
    matplot(name, saida_y, saida_x, e, d)


def matplot(name, saida_y, saida_x, tam_min, tam_max):

    #name, saida_y, saida_x, tam_min, tam_max = ping_portal()
    
    #VARIAVEIS
    nome = name
    y = saida_y
    x = saida_x
    tamMin = tam_min
    tamMax = tam_max

    #add x and y labels 
    grafico.xlabel('Tempo/Quantidade')
    grafico.ylabel('Tempo/ms')

    #Axes range
    grafico.axis(ymin=tamMin,ymax=tamMax)

    #add title
    grafico.title('Relatorio PING')
    #plot
    #grafico.plot(x, y, label=nome, marker='o')
    grafico.bar(x, y, label=nome)
    grafico.legend()
    grafico.grid(False)

    # print(nome)
    # linha()
    # print(x)
    # linha()
    # print(y)
    # linha()
    # print(tamMin, tamMax)

    #show plot
    grafico.show()




