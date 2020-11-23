
from vsg.token import interface_subprogram_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import interface_subprogram_specification
from vsg.vhdlFile.classify import interface_subprogram_default


def detect(iToken, lObjects):
    '''
    interface_subprogram_declaration ::=
        interface_subprogram_specification [ is interface_subprogram_default ]
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    iLast = iCurrent
    iCurrent = interface_subprogram_specification.detect(iCurrent, lObjects)
    if iLast != iCurrent:
        iCurrent = utils.find_next_token(iToken, lObjects)
        if utils.object_value_is(lObjects, iCurrent, 'is'):
            return classify(iCurrent, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_if('is', token.is_keyword, iToken, lObjects)
    iCurrent = interface_subprogram_default.classify(iCurrent, lObjects)

    return iCurrent
