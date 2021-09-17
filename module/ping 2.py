from  icmplib  import  ping , multiping , traceroute , resolve

address_ip = str()
count_qt = int()
interval_qt = int()
timeout_qt = int()
id_ping = int(0001)
source_ip = str()
size = int()

host = ping(address_ip, count=count_qt, interval=interval_qt, timeout=timeout_qt, id=id_ping, privileged=True)

#valores saida
#saida minima
host.min_rtt
#saida media
host.avg_rtt
#saida max
host.max_rtt

#saida em lista
host.rtts

#pacotes enviados
host.packets_sent
#pacotes recebidos
host.packets_received
#perda de pacotes
host.packet_loss

#variação Jitter
host.jitter

