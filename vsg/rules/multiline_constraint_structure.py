
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class multiline_constraint_structure(structure.Rule):
    '''
    This rule checks the structure of multiline constraints.
    '''

    def __init__(self, name, identifier):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.lTokenPairs = None

        self.record_constraint_open_paren = 'ignore'
        self.configuration.append('record_constraint_open_paren')
        self.record_constraint_close_paren = 'ignore'
        self.configuration.append('record_constraint_close_paren')
        self.record_constraint_comma = 'ignore'
        self.configuration.append('record_constraint_comma')
        self.record_constraint_element = 'ignore'
        self.configuration.append('record_constraint_element')
        self.array_constraint = 'ignore'
        self.configuration.append('array_constraint')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:

            _check_record_constraint_open_paren(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction['action'] == 'add_new_line':
            _fix_add_new_line(oViolation)
        elif dAction['action'] == 'remove_new_line':
            _fix_remove_new_line(oViolation)


def _fix_add_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    rules_utils.insert_whitespace(lTokens, 0)
    rules_utils.insert_carriage_return(lTokens, 0)
    oViolation.set_tokens(lTokens)


def _fix_remove_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    lTokens.insert(0, lTokens.pop())
    utils.remove_consecutive_whitespace_tokens(lTokens)
    lNewTokens = utils.remove_trailing_whitespace(lTokens)
    utils.fix_blank_lines(lNewTokens)
    oViolation.set_tokens(lNewTokens)


def _check_record_constraint_open_paren(self, oToi):

    if self.record_constraint_open_paren == 'ignore':
        return
    elif self.record_constraint_open_paren == 'add_new_line':
        _check_add_new_line(self, oToi, token.record_constraint.open_parenthesis)
    elif self.record_constraint_open_paren == 'remove_new_line':
        _check_remove_new_line(self, oToi, token.record_constraint.open_parenthesis)


def _check_add_new_line(self, oToi, oTokenType):

    iLine, lTokens = rules_utils.get_toi_parameters(oToi)

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, oTokenType):
            if not _token_at_beginning_of_line(iToken, lTokens):
                sSolution = 'Move parenthesis to next line.'
                oViolation = _create_violation(oToi, iLine, iToken, iToken, 'add_new_line', sSolution)
                self.add_violation(oViolation)


def _check_remove_new_line(self, oToi, oTokenType):

    iLine, lTokens = rules_utils.get_toi_parameters(oToi)

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, oTokenType):
            if _token_at_beginning_of_line(iToken, lTokens):
                sSolution = 'Move parenthesis to previous line.'
                iStart = utils.find_previous_non_whitespace_token(iToken - 1, lTokens) + 1
                oViolation = _create_violation(oToi, iLine, iStart, iToken, 'remove_new_line', sSolution)
                self.add_violation(oViolation)


def _token_at_beginning_of_line(iToken, lTokens):
    if isinstance(lTokens[iToken - 1], parser.carriage_return) or isinstance(lTokens[iToken - 2], parser.carriage_return):
        return True
    return False


def _create_violation(oToi, iLine, iStartIndex, iEndIndex, sAction, sSolution):
    dAction = _create_action_dictionary(sAction)
    oViolation = violation.New(iLine, oToi.extract_tokens(iStartIndex, iEndIndex), sSolution)
    oViolation.set_action(dAction)
    return oViolation

def _create_action_dictionary(sAction):
    dReturn = {}
    dReturn['action'] = sAction
    return dReturn
