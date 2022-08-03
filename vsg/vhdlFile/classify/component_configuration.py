
from vsg.token import component_configuration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import component_specification
from vsg.vhdlFile.classify import binding_indication
from vsg.vhdlFile.classify import block_configuration


def detect(iToken, lObjects):

    if utils.is_next_token('for', iToken, lObjects):
        iCurrent = utils.find_next_token(iToken, lObjects) + 1
        if component_specification.detect(iCurrent, lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    '''
    component_configuration ::=
        for component_specification
            [ binding_indication ; ]
            { verification_unit_binding_indication ; }
            [ block_configuration ]
        end for ;
    '''

    iCurrent = utils.assign_next_token_required('for', token.for_keyword, iToken, lObjects)

    iCurrent = component_specification.classify(iCurrent, lObjects)

    iPrevious = iCurrent
    iCurrent = binding_indication.detect(iCurrent, lObjects)
    if not iPrevious == iCurrent:
        iCurrent = utils.assign_next_token_required(';', token.binding_indication_semicolon, iCurrent, lObjects)

    iCurrent = block_configuration.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('for', token.end_for_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
