
from time import sleep
import time
from icmplib import ICMPv4Socket, ping
from icmplib import ICMPLibError, ICMPError, TimeoutExceeded
import re
import subprocess

ipv4 = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

dados_json = {
            "name" : [],
            "host" : [],
            "ipRst": []
            }

def tracert(ip, name):
    c=1
    dados_json['name'] = (name)
    dados_json['host'] = (ip)

    for host in ip:
        try: 
            print(f'Rastreando a rota para {ip} com no máximo 30 saltos')

            tracert = subprocess.Popen(
                    "tracert /d /h 30 " + host,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)

            lines = tracert.stdout.readlines()
            res = b''.join(lines).decode("utf-8", "ignore")
            
            result = re.findall(ipv4, res)[1:]

            print(f'{c} {result}')

            for ip in result:

                dados_json["ipRst"].append(ip)
            c += 1

        except subprocess.TimeoutExpired:
            print('***')

    ping_IP(True)

def ping_IP(st):
    
    #VARIAVEIS
    c = 1
    contacts = {
        "host1":{
            "num": [],
            "host": [], 
            "loss": [], 
            "sent": [], 
            "recv": [], 
            "avg": [],
            "best": [],
            "worst": [],
            "last": [],
            "jitter": [],
            "hora": []
            }}
    if st == True:
        countl=10000
    else:
        countl=0
    
    print(f'{"N"}   {"Host"}            {"Loss%"}     {"Sent"}     {"Recv"}     {"Avg"}       {"Best"}      {"Worst"}       {"Last:"}      {"Jitter"}       {"Hora":}')

    while st == True:
        for ip in dados_json["ipRst"]:
            try:
                datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

                # Enviamos o pedido
                request = ping(ip, count=1)

                # Estamos aguardando o recebimento de uma resposta do ICMP
                #reply = sock.receive(request, timeout)

                # Lançamos uma exceção se for uma mensagem de erro ICMP
                #reply.raise_for_status()

                # Exibimos algumas informações
                

                #MANPULANDO SAIDA
                address_s = request.address
                min_rtt = float('{:.3f}'.format(request.min_rtt))
                avg_rtt = float('{:.3f}'.format(request.avg_rtt))
                max_rtt = float('{:.3f}'.format(request.max_rtt))
                rtts_1 = request.rtts
                #rtts = float('{:.0f}'.format(rtts_1[0]))
                packets_sent = request.packets_sent
                packets_received = request.packets_received
                packet_loss = request.packet_loss
                jitter = request.jitter
                is_alive = request.is_alive
                loss = packets_sent * packet_loss
                

                # Exibimos algumas informações

                print(f'{c}   {address_s}          {loss}       {packets_sent}        {packets_received}     {avg_rtt}       {min_rtt}     {max_rtt}       {rtts_1}      {jitter}       {datetime}')
                sleep(2)
                c += 1
            except TimeoutExceeded:
                # O tempo limite foi atingido
                print('  Request timeout for icmp_seq ***')

            except ICMPError as err:
                # Uma mensagem de erro ICMP foi recebida
                print(err)

            except ICMPLibError:
                # Todos os outros erros
                print('  An error has occurred.')
    print('\nCompleted.')

tracert('8.8.8.8', 'portal 2')
