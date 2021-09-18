from  icmplib  import  ping
from module import *

def ping_dns():

    address_portal = "8.8.8.8"
    count_qt = 10
    interval_qt = 0.2

    host = ping(address_portal, count=count_qt, interval=interval_qt)

    valor = host.rtts
    print(host)
