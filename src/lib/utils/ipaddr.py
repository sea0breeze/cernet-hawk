import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def iplookup(ip):
    return gi.record_by_addr(ip)

if __name__ == '__main__':
    print iplookup(raw_input('ip: '))
