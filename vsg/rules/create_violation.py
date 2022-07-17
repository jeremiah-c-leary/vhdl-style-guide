
from vsg import violation

from vsg.rules import tokens_of_interest as toi

from vsg.vhdlFile import utils


def add_new_line(oToi):
    iToken = oToi.get_meta_data('iToken')

    oToi.set_meta_data('iStart', iToken)
    oToi.set_meta_data('sSolution', 'Move parenthesis to next line.')
    oToi.set_meta_data('sAction', 'add_new_line')
    toi.adjust_start_index_based_on_whitespace(oToi, -1)
    oViolation = _create_violation(oToi)
    return oViolation


def remove_new_line(self, oToi):
    iToken = oToi.get_meta_data('iToken')
    lTokens = oToi.get_tokens()

    oToi.set_meta_data('sSolution', 'Move parenthesis to previous line.')
    oToi.set_meta_data('sAction', 'remove_new_line')
    oToi.set_meta_data('iStart', utils.find_previous_non_whitespace_token(iToken - 1, lTokens) + 1)
    oViolation = _create_violation(oToi)
    return oViolation


def _create_violation(oToi):
    iStartIndex = oToi.get_meta_data('iStart')
    iStartLine = oToi.get_meta_data('iStartLine')
    iEndIndex = oToi.get_meta_data('iToken')
    sSolution = oToi.get_meta_data('sSolution')
    sAction = oToi.get_meta_data('sAction')
    lTokens = oToi.get_tokens()

    dAction = _create_action_dictionary(sAction)
    oViolation = violation.New(iStartLine, oToi.extract_tokens(iStartIndex, iEndIndex), sSolution)
    oViolation.set_action(dAction)
    return oViolation


def _create_action_dictionary(sAction):
    dReturn = {}
    dReturn['action'] = sAction
    return dReturn
