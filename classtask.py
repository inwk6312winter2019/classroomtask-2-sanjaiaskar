"""class ipaddr():
  def __init__(self,ip=[0,0,0,0],nm=[0,0,0,0]):
    self.ip=ip
    self.nm=nm
  def __str__(self):
    ipformat=""
    for ips in self.ip:
      ipformat=ipformat+"."+str(ips)

    print("the address is"+ipformat)

myip=ipaddr([192,168,1,1],[255,255,255,0])
print(myip)"""
# subnet calculator66
import sys

def _dec_to_binary(ip_address):
    return map(lambda x: bin(x)[2:].zfill(8), ip_address)


def _negation_mask(net_mask):
    wild = list()
    for i in net_mask:
        wild.append(255 - int(i))
    return wild


class IPCalculator(object):
    def __init__(self, ip_address, cdir=24):
        if '/' in ip_address:
            self._address_val, self._cidr = ip_address.split('/')
            self._address = map(int, self._address_val.split('.'))
        else:
            self._address = map(int, ip_address.split('.'))
            self._cidr = cdir
        self.binary_IP = _dec_to_binary(self._address)
        self.binary_Mask = None
        self.negation_Mask = None
        self.network = None
        self.broadcast = None

    def __repr__(self):
        print ("Calculating the IP range of %s/%s" % (".".join(map(str, self._address)), self._cidr))
        print ("=================================="
        print ("Netmask %s" % (".".join(map(str, self.net_mask()))))
        print ("Network ID %s" % (".".join(map(str, self.network_ip()))))
        print ("Subnet Broadcast address %s" % (".".join(map(str, self.broadcast_ip()))))
        print "Host range %s" % (self.host_range()))
        print "Max number of hosts %s" % (self.number_of_host()))

    def net_mask(self):
        mask = [0, 0, 0, 0]
        for i in range(int(self._cidr)):
            mask[i / 8] += 1 << (7 - i % 8)
        self.binary_Mask = _dec_to_binary(mask)
        self.negation_Mask = _dec_to_binary(_negation_mask(mask))
        return mask

    def broadcast_ip(self):
        broadcast = list()
        for x, y in zip(self.binary_IP, self.negation_Mask):
            broadcast.append(int(x, 2) | int(y, 2))
        self.broadcast = broadcast
        return broadcast

    def network_ip(self):
        network = list()
        for x, y in zip(self.binary_IP, self.binary_Mask):
            network.append(int(x, 2) & int(y, 2))
        self.network = network
        return network

    



