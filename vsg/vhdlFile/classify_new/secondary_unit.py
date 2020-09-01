
from vsg.vhdlFile.classify_new import architecture_body
#from vsg.vhdlFile.classify_new import package_body


def detect(iCurrent, lObjects):
    '''
    secondary_unit ::= 
        architecture_body
      | package_body
    '''
    iReturned = architecture_body.detect(iCurrent, lObjects)
    if iReturned != iCurrent:
        return iReturned

#    iReturned = package_body.detect(iCurrent, lObjects)
#    if iReturned != iCurrent:
#        return iReturned

    return iCurrent
