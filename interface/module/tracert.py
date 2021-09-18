from icmplib import traceroute

def tracert(portal):
    hops = traceroute(portal)

    print('Distance/TTL    Address    Average round-trip time')
    last_distance = 0

    for hop in hops:
        if last_distance + 1 != hop.distance:
            print('Some gateways are not responding')

    # See the Hop class for details
        print(f'{hop.distance}    {hop.address}    {hop.avg_rtt} ms')

        last_distance = hop.distance
    print(hops)
