import re
import subprocess
import  json
import time
import pandas as pd
import os
from multiprocessing import Process
from time import sleep
from icmplib import ping
from icmplib import TimeoutExceeded
from icmplib import ICMPv4Socket

class mtrTrace():
    def start(self, name, dst, st):
        """"""
        # Dicionario
        self.dados = {
            "name" : name, #nome
            "host" : dst, #Host
            }
    
        self.ping_out = {
                "name" : name, #nome
                "host" : dst, #Host
                "ipRst": [], #Ip
                "all_pct":[], #Todos os pct
                "time": [], #hora
                "mtr": [] #mtr
                }
        # Manter ping
        self.st = st

        self.tracert(self, name, dst)

    def tracert(self, name, dst):
        """"""
        name = name
        dst = dst
        c=1
        ipv4 = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        host = self.ping_out["ipRst"]

        print(f'\nRastreando a rota para {dst} com no máximo 30 saltos')
        try: 
            tracert = subprocess.Popen(
                    "tracert /d /h 30 " + dst,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)

            lines = tracert.stdout.readlines()
            res = b''.join(lines).decode("utf-8", "ignore")
            
            result = re.findall(ipv4, res)[1:]

        except subprocess.TimeoutExpired:
            print('***')

        print('\nExibindo resultados.')
        for ip in result:
            #Escrever na tela e add a list
            print(f'{c} - {ip}')
            c += 1
        
        #Adicionando valores a lista
        print('\nAdicionando valores a lista.')
        for p in result:
            self.ping_out["ipRst"].append(p)
            self.ping_out["all_pct"].append([])
            self.ping_out["time"].append([])
            self.ping_out["mtr"].append([])

        print(self.ping_out)
        self.tarefa(self, host)

    def tarefa(self, host):
        """"""
        host = host
        id = 0
        if __name__=="__main__":
            processes = []
            num_processes = os.cpu_count()

            #Criar processo e designar função
            for i in range(num_processes):
                for ip in host:
                    process = Process(target=self.pingMtr(self, ip, id))
                    processes.append(process)
                    id+=1
            print(processes)
            #Iniciar processo
            for process in processes:
                print(f'\nStart Host {host[id]}')
                process.start()
                id+=1
    
            #Verificar se os processos terminaram 
            #Bloquear o processo e finalizar.
            for process in processes:
                process.join()


    def pingMtr(self, ip, id):
        """"""
        #VARIAVEIS
        c = 1
        datetime = time.strftime('%H:%M:%S', time.localtime())
        count = self.st
        name = self.ping_out["name"]

        print(f'\nDisparando {ip} com 64 bytes de n:\n')

        for s in range(count):   
            try:
                # Enviamos o pedido
                request = ping(ip, count=3, timeout=1)
                #Adicionando valores a biblioteca

                for i in request.rtts:
                    self.ping_out["all_pct"][id].append(f'{i:.3f}')
                    sleep(0.3)
                    self.ping_out["time"][id].append(datetime)

                #MANPULANDO SAIDA
                num = c #Num
                sent = len(self.ping_out["all_pct"][id])
                recv = len(self.ping_out["all_pct"][id]) #Pct recebidos
                loss = sent%recv #Media perdas ATUALIZAR
                avg = float('{:.3f}'.format(request.avg_rtt)) #Media pct
                best = float('{:.3f}'.format(request.min_rtt)) #Melhor pct
                worst = float('{:.3f}'.format(request.max_rtt)) #Pior pct
                last = self.ping_out["all_pct"][id][-1:]
                jitter = request.jitter #Jitter
                hora = self.ping_out["time"][id][-1:] #hora

                # Exibimos algumas informações
                table = [num, ip, loss, sent, recv, avg, best, worst, last, jitter, hora]
                df2 = pd.DataFrame([table], columns=["N", "Host", "Loss%", "Sent", "Recv", "Avg", "Best", "Worst", "Last", "Jitter", "Hora"])
                print(df2)

                #Adicionando valores a biblioteca
                self.ping_out["mtr"][id] = (table)

                c += 1
                sleep(1)

            except TimeoutExceeded:
                # O tempo limite foi atingido
                print('  Request timeout for icmp_seq ***\n')

        self.createJson(self, name)

        
    def createJson(self, name):
        """"""
        print('\nGravando arquivos no json.')
        json_str = json.dumps(self.ping_out)

        print(self.ping_out)

        with open('log\log_{}.json'.format(name), 'w') as fh:
            fh.write(f'\n{json_str}')

        print('\nCompleted.')

    

dst = '8.8.8.8'
name = 'dns'

mtrTrace.start(mtrTrace, name, dst, 30)