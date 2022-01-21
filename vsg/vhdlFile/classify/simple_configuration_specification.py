
from vsg.vhdlFile import utils

from vsg.token import simple_configuration_specification as token

from vsg.vhdlFile.classify import component_specification
from vsg.vhdlFile.classify import binding_indication


def detect(iToken, lObjects):
    '''
    simple_configuration_specification ::=
        **for** component_specification binding_indication ;
        [ **end** **for** ; ]
    '''
    if utils.is_next_token('for', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = iToken

    iCurrent = utils.assign_next_token_required('for', token.for_keyword, iCurrent, lObjects)

    iCurrent = component_specification.classify(iCurrent, lObjects)
    iCurrent = binding_indication.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    if utils.is_next_token('end', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('for', token.end_for_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
