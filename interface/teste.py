def op_check1(event): #Essa função armazena os valores var do widget ccb.
    global resp_1, resp_portal
    resp_1 = ccb.get()
    resp_portal = portal_entrada[resp_1]
    lb2['text'] = "-", resp_portal

    return resp_1, resp_portal

def op_check2(c): #Essa função armazena os valores var do widget checkbox.

    resp1 = valor_check1.get()
    #resp1 = resp_1
    resp2 = valor_check2.get()
    #resp2 = resp_2
    resp3 = valor_check3.get()
    #resp3 = resp_3
    resp4 = int(len1.get())
    #resp4 = int(resp_4)
    resp5 = len2.get()
    #resp5 = resp_5
    resp6 = len3.get()
    #resp6 = resp_6

    #PING PORTAL + DNS + PING IP
    if resp_1 in portais and resp4 and resp5 and resp6 != 0 and c == "SIM" and resp2 == 1:
            next(10)
    
    #PING PORTAL + PING IP
    if resp6 != 0 and resp_1 in portais and resp5 and resp4 != 0 and c == "SIM":
            next(8)
    
    #PING PORTAL + TRACERT + PING IP
    if resp_1 in portais and resp4 and resp5 and resp6 != 0 and c == "SIM" and resp1 == 1:
            next(9)
    
    #PING PORTAL + SIP ALG + PING IP
    if resp_1 in portais and resp4 and resp5 and resp6 != 0 and c == "SIM" and resp3 == 1:
            next(11)
    
    #PING PORTAL + TRACERT + DNS + PING IP
    if resp_1 in portais and resp4 and resp5 and resp6 != 0 and c == "SIM" and resp1 and resp2 == 1:
            next(12)
    
    #PING PORTAL + TRACERT + SIP ALG + PING IP
    if resp_1 in portais and resp4 and resp5 and resp6 != 0 and c == "SIM" and resp1 and resp3 == 1:
            next(13)
   
        #PING PORTAL + TRACERT
    if resp_1 in portais and resp4 > 0 and c == "SIM"  and resp1 == 1:
            next(2)
    
    #PING PORTAL + DNS
    if resp_1 in portais and resp4 > 0 and c == "SIM" and resp2 == 1:
            next(3)
   
    #PING PORTAL + SIP ALG
    if resp_1 in portais and resp4 > 0 and c == "SIM" and resp3 == 1:
            next(4)

    #PING COM TODAS OP
    if resp_1 in portais and resp4 and resp5 and resp6 != 0 and c == "SIM" and resp1 and resp2 and resp3 == 1:
            next(14)
    
        #PING PORTAL + TRACERT + DNS
    if resp_1 in portais and resp4 > 0 and c == "SIM" and resp1 and resp2 == 1:
            next(5)
   
    #PING PORTAL + TRACERT + SIP ALG
    if resp_1 in portais and resp4 > 0 and c == "SIM" and resp1 and resp3 == 1:
            next(6)
    
    #PING COM TODAS OP
    if resp_1 in portais and resp4 > 0 and c == "SIM" and resp1 and resp2 and resp3 == 1:
            next(7)
    
    #PING PORTAL
    if resp_1 in portais and resp4 > 0 and c == "SIM":
            next(1)
    

def next(num: int): #Essa função execulta os comando, vinculada ao botao execultar. 
    resp_1 = ccb.get()
    resp4 = int(len1.get())
    resp5 = len2.get()
    resp6 = len3.get()

    if num == 1 : 
        ping_portal(resp_portal, resp4, resp_1)
    elif num == 2:
        ping_portal(resp_portal, resp4, resp_1)
        print('tracert não pronto')
    elif num == 3:
        text_area.insert(tk.INSERT, 'Iniciando coleta...')
        threading.Thread(target=ping_portal(resp_portal, resp4, resp_1)).start()
        threading.Thread(target=ping_DNS(resp4 ,'DNS Google')).start()

    elif num == 4:
        ping_portal(resp_portal, resp4, resp_1)
        sip_alg()
    elif num == 5:
        ping_portal(resp_portal, resp4, resp_1)
        ping_DNS(resp4 ,'DNS Google')
        print('tracert não pronto')
    elif num == 6:
        print('tracert não pronto')
        sip_alg()
    elif num == 7:
        ping_portal(resp_portal, resp4, resp_1)
        ping_DNS(resp4 ,'DNS Google')
        print('tracert não pronto')
        sip_alg()
    elif num == 8:
        ping_portal(resp_portal, resp4, resp_1)
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')
    elif num == 9:
        ping_portal(resp_portal, resp4, resp_1)
        print('tracert não pronto')
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')
    elif num == 10:
        ping_portal(resp_portal, resp4, resp_1)
        ping_DNS(resp4 ,'DNS Google')
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')
    elif num == 11:
        ping_portal(resp_portal, resp4, resp_1)
        sip_alg()
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')
    elif num == 12:
        ping_portal(resp_portal, resp4, resp_1)
        ping_DNS(resp4 ,'DNS Google')
        print('tracert não pronto')
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')
    elif num == 13:
        ping_portal(resp_portal, resp4, resp_1)
        ping_DNS(resp4 ,'DNS Google')
        sip_alg()
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')
    elif num == 14:
        ping_portal(resp_portal, resp4, resp_1)
        ping_DNS(resp4 ,'DNS Google')
        print('tracert não pronto')
        sip_alg()
        ping_IP(resp5, resp4, 'HOST')
        ping_IP_2(resp6, resp4, 'GATEWAY')