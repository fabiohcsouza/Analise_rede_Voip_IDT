
import time
import scapy.all as scapy
import sys
import  json
from time import sleep

class trace():
    def __init__(self, dst, name):

        # Dicionario
        self.dados_json = {
            "name" : [],
            "host" : [], 
            "numID" : [],
            "ipRst": [],
            "nPing" : [],
            "vPing": [],
        }
        # Add variaveis entrada no dicionario
        self.dados_json['name'] = (name)
        self.dados_json['host'] = (dst)

        # Call Tracert
        self.tracerouter()
    
    def tracerouter(self):
        # Valores, variavel
        name_id = self.dados_json["name"]
        dst_host = self.dados_json["host"]

        # Tracert
        ans, unans = scapy.sr(scapy.IP(dst=dst_host, ttl=(1,30),id=scapy.RandShort())/scapy.TCP(flags=0x2), timeout=10)
        
        for snd,rcv in ans:
            self.dados_json["numID"].append('{}'.format(snd.ttl))
            self.dados_json["ipRst"].append(rcv.src)

        self.createJson(name_id)

    def createJson(self, id):

        json_str = json.dumps(self.dados_json)

        print(json_str)

        with open('data{}.json'.format(id), 'w') as fh:
            fh.write(json_str)


dst = 'proxy2.idtbrasilhosted.com'
name = 'portal 2'

trace(dst, name)