
from vsg.token import iteration_scheme as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import condition
from vsg.vhdlFile.classify import parameter_specification


def detect(iToken, lObjects):
    '''
    iteration_scheme ::=
        while condition
      | for *loop*_parameter_specification
    '''
    if utils.find_in_next_n_tokens(';', 3, iToken, lObjects):
        return False
    if utils.find_in_next_n_tokens('else', 3, iToken, lObjects):
        return False
    if utils.find_in_next_n_tokens('while', 3, iToken, lObjects):
        return True
    if utils.find_in_next_n_tokens('for', 3, iToken, lObjects):
        return True
    return False


def classify(iToken, lObjects):

    if utils.is_next_token('while', iToken, lObjects):
        iCurrent = utils.assign_next_token_required('while', token.while_keyword, iToken, lObjects)
        iCurrent = condition.classify_until(['loop'], iToken, lObjects)
        return iCurrent

    if utils.is_next_token('for', iToken, lObjects):
        iCurrent = utils.assign_next_token_required('for', token.for_keyword, iToken, lObjects)
        iCurrent = parameter_specification.classify_until(['loop'], iToken, lObjects)
        return iCurrent

    return iToken
