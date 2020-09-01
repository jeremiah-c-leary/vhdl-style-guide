
#from vsg.vhdlFile.classify_new import primary_unit
from vsg.vhdlFile.classify_new import secondary_unit


def detect(iCurrent, lObjects):
    '''
    library_unit ::=
        primary_unit
      | secondary_unit
    '''
#    iReturned = primary_unit.detect(iCurrent, lObjects)
#    if iReturned != iCurrent:
#        return iReturned

    iReturned = secondary_unit.detect(iCurrent, lObjects)
    if iReturned != iCurrent:
        return iReturned

    return iCurrent
