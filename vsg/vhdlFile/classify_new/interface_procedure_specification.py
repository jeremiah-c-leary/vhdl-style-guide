
from vsg.vhdlFile.classify_new import formal_parameter_list

from vsg.token import interface_procedure_specification as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    interface_procedure_specification ::=
        procedure designator
            [ [ parameter ] ( formal_parameter_list ) ]
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'procedure'):
        return classify(iCurrent, lObjects)
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
