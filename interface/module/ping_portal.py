#from module.matplotlib import controle




"""FUNÇÕES SISTEMA"""

from  icmplib  import  ping
import matplotlib.pyplot as grafico


def ping_portal(portal, tm):
    address_portal = portal
    interval_qt = 0.1

    host1 = ping(address_portal, count=tm, interval=interval_qt)

    # with open('log\ping\ping_portal_result.log', 'w') as f:
    #     f.write(host1)

    valor1 = host1.rtts
    # min = host1.min_rtt
    max = host1.max_rtt
    a = ['{:.0f}'.format(i) for i in valor1]
    d = int('{:.0f}'.format(max))

    a_sort = list(range(1,41))

    #text_area.insert(tk.INSERT, host1)
    print(host1)

    print('Valores ping: {} '.format(a))

    print(a_sort)

    return a, a_sort, d


def ping_dns(tm):

    address_portal = "8.8.8.8"
    interval_qt = 0.2

    host2 = ping(address_portal, count=tm, interval=interval_qt)

    # with open('log\ping\ping_dns_result.log', 'w') as f:
    #     for a in host2:
    #         f.write('{:.0f}'.format((a)))

    valor2 = host2.rtts
    a = ['{:.0f}'.format(i) for i in valor2]
    a_sort = a.sort()

    #text_area.insert(tk.INSERT, host)

    # with open('log\ping\ping_dns_list.log', 'w') as f:
    #     for a in valor2:
    #         f.write('{:.0f}\n'.format((a)))
    return a, a_sort

def ping_ip(ip, tm, nome):
    address_ip = ip
    interval_qt = 0.2
    name = nome

    host3 = ping(address_ip, count=tm, interval=interval_qt)

    with open('log\ping\ping_{}_result.log', 'w'.format(name)) as f:
        for a in host3:
            f.write('{:.0f}'.format((a)))

    valor1 = host3.rtts

    #text_area.insert(tk.INSERT, host1)
    
    with open('log\ping\ping_{}_list.log', 'w'.format(name)) as f:
        for a in valor1:
            f.write('{:.0f}\n'.format((a)))


def matplot(list_s, list2_s,d):
    Y = list_s
    X = list2_s

    #plot
    grafico.scatter(X, Y, s=60, c='red', marker='o')

    #Axes range
    grafico.xlim(0,40)
    grafico.ylim(0,d)

    #add title
    grafico.title('Relatorio PING')

    #add x and y labels 
    grafico.xlabel('Tempo/Quantidade')
    grafico.ylabel('Tempo/ms')

    #show plot
    grafico.show()


a, b, d = ping_portal("proxy10.idtbrasilhosted.com", 40)

c = ping_dns(20)

matplot(a, b, d)