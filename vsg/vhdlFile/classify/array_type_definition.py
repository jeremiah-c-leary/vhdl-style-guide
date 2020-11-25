
from vsg.vhdlFile.classify import constrained_array_definition
from vsg.vhdlFile.classify import unbounded_array_definition


def detect(iToken, lObjects):
    '''
    array_type_definition ::=
        unbounded_array_definition
      | constrained_array_definition
    '''

    iCurrent = unbounded_array_definition.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = constrained_array_definition.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
