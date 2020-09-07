

from vsg.vhdlFile.classify_new import array_type_definition
#from vsg.vhdlFile.classify_new import record_type_definition

'''
    composite_type_definition ::=
        array_type_definition
      | record_type_definition
'''


def detect(iToken, lObjects):

    iReturn = array_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    iReturn = record_type_definition.detect(iToken, lObjects)
#    if iReturn != iToken:
#        return iReturn

    return iToken
