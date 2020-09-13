
from vsg.token import subprogram_kind as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    subprogram_kind ::=
        procedure | function
    '''

    if utils.is_next_token('procedure', iToken, lObjects):
        return True
    if utils.is_next_token('function', iToken, lObjects):
        return True
    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_if('procedure', token.procedure_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('function', token.function_keyword, iToken, lObjects)

    return iCurrent
