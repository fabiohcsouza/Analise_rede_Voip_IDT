from module.matplotlib import controle
from  icmplib  import  ping
from module import *

def ping_portal(portal: str):
    address_portal = portal
    count_qt = 10
    interval_qt = 0.2
    c = (1000)

    host = ping(address_portal, count=count_qt, interval=interval_qt)

    valor = host.rtts
    print(host)
    controle(valor)

ping_portal("8.8.8.8")
