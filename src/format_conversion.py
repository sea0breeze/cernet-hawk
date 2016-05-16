import config
def Conversion(portfile, ipfile):
    ipdict = {}
    inputfile = open(portfile)

    for line in inputfile:
        line = line.split()
        port = line[0]
        iplist = line[1:]
        for ip in iplist:
            if ip in ipdict:
                ipdict[ip] += [port]
            else:
                ipdict[ip] = [port]

    inputfile.close()

    outputfile = open(ipfile, 'w')
    for ip in ipdict:
        line = ' '.join([ip] + ipdict[ip]) + '\n'
        outputfile.write(line)
    outputfile.close()

if __name__ == "__main__":
    Conversion("port.txt", "ip.txt")
