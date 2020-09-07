

from vsg.vhdlFile.classify_new import unbounded_array_definition
from vsg.vhdlFile.classify_new import constrained_array_definition

'''
    array_type_definition ::=
        unbounded_array_definition
      | constrained_array_definition
'''


def detect(iToken, lObjects):

    iReturn = unbounded_array_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = constrained_array_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
