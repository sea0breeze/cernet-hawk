import config

ipdict = {}
inputfile = open(config.PORTFILE_PATH)

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

outputfile = open(config.IPFILE_PATH, 'w')
for ip in ipdict:
    line = ' '.join([ip] + ipdict[ip]) + '\n'
    outputfile.write(line)

outputfile.close()
