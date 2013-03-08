import os
import transmissionrpc

ips = ['192.168.1.93', '192.168.1.84', '192.168.1.106','192.168.1.102', '192.168.1.91']
computersOnline = []


tc = transmissionrpc.Client('<ip>', port=9091,user='',password='')

for ip in ips:
    ret = os.system("ping -q -c 3 -W 3 " + ip)
    if ret == 0:
        computersOnline.append(ip);


if len(computersOnline) == 0:
    args = {'alt_speed_enabled' : 'false'}
else:
    args = {'alt_speed_enabled' : 'true'}

tc.set_session(None, **args);