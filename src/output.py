import json
import pprint
  
def output(outputdict,outputformat,outputfile):
    outfile = open(outputfile, 'w')
    if(outputformat=='json'):
        outfile.write(json.dumps(outputdict))
    if(outputformat=='pprint'):
       outfile.write(pprint.pformat(outputdict))
    outfile.close()
    

