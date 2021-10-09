import re
import subprocess
import  json
import time
import pandas as pd
import multiprocessing
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
                print(self.c ,' - ', ip)

                sleep(1)
                self.c += 1

        except subprocess.TimeoutExpired:
            print('***')

        self.c = 1
        print(self.dados_json)

        self.multiProcess()

    def multiProcess(self):
        if __name__ == '__main__':
            self.jobs = []
            for i in range(len(self.dados_json["ipRst"])):
                for ip in self.dados_json["ipRst"]:
                    p = multiprocessing.Process(target=self.ping_IP(ip))
                    self.jobs.append(p)
                    p.start()
                sleep(1)

    def ping_IP(self, ip):
        count = 10
        c = 1
        if self.st == True:
            count += 1
        else:
            count=0

        for sequence in range(count):

            try:
                # Enviamos o pedido
                request = ping(ip, count=count, timeout=1)

                #Adicionando valores a biblioteca
                self.dados_json["hora"].append(self.datetime)
                self.dados_json["all_pct"].append(request.rtts)

                #MANPULANDO SAIDA
                num = c #Num
                sent = request.packets_sent
                loss = '#0' #len(self.dados_json["all_pct"]) #Media perdas ATUALIZAR
                recv = len(self.dados_json["all_pct"]) #Pct recebidos
                avg = request.avg_rtt
                best = request.min_rtt #Melhor pct
                worst = request.max_rtt #Pior pct
                last = '{:.0f}'.format(self.dados_json["all_pct"[0]])
                jitter = request.jitter #Jitter
                hora = self.datetime #hora

                #Adicionando valores a biblioteca
                #self.dados_json["mtr"].append(self.out_ping)

                # Exibimos algumas informações
                table = [num, ip, loss, sent, recv, avg, best, worst, last, jitter, hora]
                df2 = pd.DataFrame([table], columns=["N", "Host", "Loss%", "Sent", "Recv", "Avg", "Best", "Worst", "Last", "Jitter", "Hora"])
                print(df2)

                sleep(1)
                c += 1

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


