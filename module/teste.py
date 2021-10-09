import re
import subprocess
import  json
import time
import fractions
from time import sleep
from icmplib import ping
from icmplib import TimeoutExceeded

class mtrTrace():
    def __init__(self, dst, name, st):

        # Dicionario
        self.dados_json = {
            "name" : [], #nome
            "host" : [], #Host
            "ipRst": [], #Ip
            "all_pct": [], #Todos os pct
            "mtr": [], #Pct enviados
            "hora": [] #hora
            }

        # Var manter ping
        self.st = st
        self.c = 1
        # Add variaveis entrada no dicionario
        self.dados_json['name'] = (name)
        self.dados_json['host'] = (dst)
        # Var 
        self.ip = self.dados_json["host"]
        self.name_id = self.dados_json["name"]
        self.datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # Call Tracert
        self.tracerouter(self.ip)
    

    def tracerouter(self, ip):

        # Valores, variavel
        self.ipv4 = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

        print(f'Rastreando a rota para {ip} com no máximo 30 saltos')

        try:  
            tracert = subprocess.Popen(
                    "tracert /d /h 30 " + ip,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)

            lines = tracert.stdout.readlines()
            res = b''.join(lines).decode("utf-8", "ignore")
            
            result = re.findall(self.ipv4, res)[1:]

            for ip in result:
                self.dados_json["ipRst"].append(ip)

            sleep(1)
            self.c += 1

        except subprocess.TimeoutExpired:
            print('***')

        self.c = 1
        print(self.dados_json)

        self.ping_IP()

    def ping_IP(self):

        # Escrever na tela
        print(f'{"N"}   {"Host"}            {"Loss%"}     {"Sent"}     {"Recv"}     {"Avg"}       {"Best"}      {"Worst"}       {"Last:"}      {"Jitter"}       {"Hora":}')

        while self.st == True:
            for ip in self.dados_json["ipRst"]:
                try:

                    # Enviamos o pedido
                    request = ping(ip, count=1, timeout=1)

                    #Adicionando valores a biblioteca
                    self.dados_json["hora"].append(self.datetime)
                    self.dados_json["all_pct"].append(request.rtts)

                    #MANPULANDO SAIDA
                    self.num = self.c #Num
                    self.sent = 1 #Pct enviados
                    self.loss = self.sent/len(self.dados_json["all_pct"]) #Media perdas
                    self.recv = len(self.dados_json["all_pct"]) #Pct recebidos
                    self.avg = self.recv #Media pct ATUALIZAR
                    self.best = min(self.dados_json["all_pct"]) #Melhor pct
                    self.worst = max(self.dados_json["all_pct"]) #Pior pct
                    self.last = self.dados_json["all_pct"][0] #Ultimo pc
                    self.jitter = request.jitter #Jitter
                    self.hora = self.datetime #hora
                    self.out_ping = (f'{self.num}, {ip}, {self.loss}, {self.sent}, {self.recv}, {self.avg}, {self.best}, {self.worst}, {self.last}, {self.jitter}, {self.datetime}')
                    self.dados_json["mtr"].append(self.out_ping)

                    # Exibimos algumas informações
                    print(f'{self.num}, {ip}, {self.loss}, {self.sent}, {self.recv}, {self.avg}, {self.best}, {self.worst}, {self.last}, {self.jitter}, {self.datetime}')

                    sleep(1)

                    self.c += 1
                    self.sent += 1
                except TimeoutExceeded:
                    # O tempo limite foi atingido
                    print('***')

        print(self.host1)

        def createJson(self, id):

            json_str = json.dumps(self.dados_json)

            print(json_str)

            with open('data_{}.json'.format(id), 'w') as fh:
                fh.write(json_str)

dst = '8.8.8.8'
name = 'portal 2'

mtrTrace(dst, name, True)


