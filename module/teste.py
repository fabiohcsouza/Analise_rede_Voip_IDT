
import time
import scapy.all as scapy
import sys
import  json
from time import sleep

class trace():
    def __init__(self, dst):

        self.dst = dst
        self.name = 'P2'

        self.dados_json  =  {
        "name" : [] ,
        "host" : [] , 
        "num" : [] , 
        "ip" : [] , 
        } 

        for h in self.dst:
            a, b = scapy.sr(scapy.IP(dst=h, ttl=(1,30),id=scapy.RandShort())/scapy.TCP(flags=0x2), timeout=10)
        
            for snd, rcv  in a:
                self.dados_json['num'].append('{}'.format(snd.ttl))
                self.dados_json['ip'].append(rcv.src)

            for nm in self.name:
                self.dados_json['name'] = (self.name)

            for dst in self.dst:
                self.dados_json['host'] = (self.dst)
        for i in self.name:
            self.Json(i)
    

    def Json(self, name):

        json_str = json.dumps(self.dados_json) 

        with open('data{}.json'.format(name), 'w') as fh:
            fh.write(json_str)

portal_list = ('proxy2.idtbrasilhosted.com' ,'8.8.8.8')
name_list = ('portal 2', 'dns google')


trace(portal_list)