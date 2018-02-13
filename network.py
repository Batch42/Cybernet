from socket import *
from Crypto.PublicKey import RSA
import random

serv= socket(AF_INET, SOCK_DGRAM)
serv.bind(('', 0))
cli= socket(AF_INET, SOCK_DGRAM)
key=RSA.importKey(open('key.rsa').read())

class Peer(object):
    """docstring for Peer."""
    def __init__(self, pub,name,ip):
        super(Peer, self).__init__()
        self.pub = RSA.importKey(pub)
        self.name = name
        self.addr = (ip,self.findPort())

    def send(self,m):
        global cli
        global key
        cli.sendto(self.pub.encrypt(key.decrypt(m), long(random.randInt(1,999999))).encode(),self.addr)
