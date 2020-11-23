
from vsg.token import interface_procedure_specification as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import formal_parameter_list


def detect(iToken, lObjects):
    '''
    interface_procedure_specification ::=
        procedure designator
            [ [ parameter ] ( formal_parameter_list ) ]
    '''
    if utils.is_next_token('procedure', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('procedure', token.procedure_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.designator, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('parameter', token.parameter_keyword, iCurrent, lObjects)

    if utils.is_next_token('(', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
        iCurrent = formal_parameter_list.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
