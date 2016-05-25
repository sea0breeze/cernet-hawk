import json
import pprint
  
def output(outputdict,outputformat,outputfile):
    '''
    Output a dictionary in the form of json or pprint
    :param outputdict: dict. the output dictionary
    :param outputformat: str. the form of output, must be one of ['j','json','p','pprint']
    :param outputfile: str. the name of outputfile
    '''
    outfile = open(outputfile, 'w')
    if(outputformat in ('j', 'json')):
        outfile.write(json.dumps(outputdict))
    if(outputformat in ('p', 'pprint')):
       outfile.write(pprint.pformat(outputdict))
    outfile.close()
    

