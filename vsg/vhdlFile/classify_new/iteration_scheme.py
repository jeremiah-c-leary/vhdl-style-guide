
from vsg.token import iteration_scheme as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import condition
from vsg.vhdlFile.classify_new import parameter_specification

'''
    iteration_scheme ::=
        while condition
      | for *loop*_parameter_specification
'''


def detect(iToken, lObjects):
    if utils.find_in_next_n_tokens('while', 3, iToken, lObjects):
        return True
    if utils.find_in_next_n_tokens('for', 3, iToken, lObjects):
        return True
    return False


def classify(iToken, lObjects):

    iCurrent = iToken

    if utils.is_next_token('while', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('while', token.while_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until('loop', iToken, lObjects)

    if utils.is_next_token('for', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('for', token.for_keyword, iCurrent, lObjects)
        iCurrent = parameter_specification.classify_until('loop', iToken, lObjects)

    return iCurrent
