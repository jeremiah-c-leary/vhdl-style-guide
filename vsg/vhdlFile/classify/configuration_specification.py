
from vsg.vhdlFile.classify import simple_configuration_specification


def detect(iToken, lObjects):
    '''
    configuration_specification ::=
        simple_configuration_specification
      | compound_configuration_specification
    '''
    iReturn = simple_configuration_specification.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
