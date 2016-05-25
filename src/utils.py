import config

def conversion(keydict):
    valuedict = {}
    for key in keydict.keys():
        valuelist = keydict[key]
        #print valuelist
        for element in valuelist:
            if element in valuedict:
                valuedict[element] += [key]
            else:
                valuedict[element] = [key]
    return valuedict


if __name__ == "__main__":
    keydict = {'80':['202.120.61.34', '202.120.24.151', '202.120.49.25', '202.120.25.239', '202.120.63.184', '202.120.1.7'],'443':['202.120.24.43', '202.120.46.2', '202.120.1.26', '202.120.53.107', '202.120.34.3', '202.120.32.61', '202.120.53.235', '202.120.44.244', '202.120.52.38', '202.120.46.9', '202.120.35.239', '202.120.33.137']}
    print conversion(keydict)
