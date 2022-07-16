
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rules import create_violation
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class multiline_procedure_call_structure(structure.Rule):
    '''
    This rule checks the structure of multiline constraints.
    '''

    def __init__(self, name, identifier):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.lTokenPairs = None

        self.first_open_paren = 'ignore'
        self.configuration.append('first_open_paren')
        self.last_close_paren = 'ignore'
        self.configuration.append('last_close_paren')
        self.association_list_comma = 'ignore'
        self.configuration.append('association_list_comma')
        self.association_element = 'ignore'
        self.configuration.append('association_element')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:

            _check_first_open_paren(self, oToi)
            _check_last_close_paren(self, oToi)
            _check_association_list_comma(self, oToi)
            _check_association_element(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction['action'] == 'add_new_line':
            _fix_add_new_line(oViolation)
        elif dAction['action'] == 'remove_new_line':
            _fix_remove_new_line(oViolation)
        elif dAction['action'] == 'add_new_line_and_remove_carraige_returns':
            _fix_add_new_line_and_remove_carraige_returns(oViolation)


def _fix_add_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    rules_utils.remove_leading_whitespace_tokens(lTokens)
    rules_utils.insert_whitespace(lTokens, 0)
    rules_utils.insert_carriage_return(lTokens, 0)
    oViolation.set_tokens(lTokens)


def _fix_add_new_line_and_remove_carraige_returns(oViolation):
    lTokens = oViolation.get_tokens()
    lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
    rules_utils.remove_leading_whitespace_tokens(lTokens)
    rules_utils.insert_whitespace(lTokens, 0)
    rules_utils.insert_carriage_return(lTokens, 0)
    rules_utils.change_all_whitespace_to_single_character(lTokens)
    utils.fix_blank_lines(lTokens)
    oViolation.set_tokens(lTokens)


def _fix_remove_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
    utils.remove_consecutive_whitespace_tokens(lTokens)
    rules_utils.remove_leading_whitespace_tokens(lTokens)
    rules_utils.change_all_whitespace_to_single_character(lTokens)
    lNewTokens = utils.remove_trailing_whitespace(lTokens)
    utils.fix_blank_lines(lNewTokens)
    oViolation.set_tokens(lNewTokens)


def _check_first_open_paren(self, oToi):

    _check_add_new_line_and_remove_new_line(self, oToi, self.first_open_paren, token.procedure_call.open_parenthesis)


def _check_last_close_paren(self, oToi):

    _check_add_new_line_and_remove_new_line(self, oToi, self.last_close_paren, token.procedure_call.close_parenthesis)


def _check_association_list_comma(self, oToi):

    _check_add_new_line_and_remove_new_line(self, oToi, self.association_list_comma, token.association_list.comma)


def _check_association_element(self, oToi):

    _check_add_new_line_and_remove_new_line(self, oToi, self.association_element, token.association_element.formal_part)


def _check_add_new_line_and_remove_new_line(self, oToi, sOption, oTokenType):
    if sOption == 'ignore':
        return
    elif sOption == 'add_new_line':
        analyze_with_function(self, oToi, oTokenType, analyze_add_new_line)
    elif sOption == 'remove_new_line':
        analyze_with_function(self, oToi, oTokenType, analyze_remove_new_line)


def analyze_with_function(self, oToi, oTokenType, fFunction):
    iLine, lTokens = rules_utils.get_toi_parameters(oToi)

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, oTokenType):
            oToi.set_meta_data('iStartLine', iLine)
            oToi.set_meta_data('iStart', iToken)
            oToi.set_meta_data('iToken', iToken)
            fFunction(self, oToi)


def analyze_add_new_line(self, oToi):
    iToken = oToi.get_meta_data('iToken')
    lTokens = oToi.get_tokens()
    if not rules_utils.token_at_beginning_of_line_in_token_list(iToken, lTokens):
        oViolation = create_violation.add_new_line(oToi)
        self.add_violation(oViolation)


def analyze_remove_new_line(self, oToi):
    iToken = oToi.get_meta_data('iToken')
    lTokens = oToi.get_tokens()
    if rules_utils.token_at_beginning_of_line_in_token_list(iToken, lTokens):
        oViolation = create_violation.remove_new_line(self, oToi)
        self.add_violation(oViolation)


def first_open_paren_detected(oToi, iLine, oToken):
    if isinstance(oToken, token.record_constraint.open_parenthesis):
        oToi.set_meta_data('iStart', oToi.get_meta_data('iToken'))
        oToi.set_meta_data('iStartLine', iLine)


def last_close_paren_detected(self, oToi, oToken):
    if isinstance(oToken, token.record_constraint.close_parenthesis):
        lTokens = oToi.get_tokens()
        iStart = oToi.get_meta_data('iStart')
        iToken = oToi.get_meta_data('iToken')
        if rules_utils.number_of_carriage_returns(lTokens[iStart:iToken]) > 0:
            oViolation = create_array_constraint_remove_carriage_return_violation(oToi)
            self.add_violation(oViolation)


def filter_tokens(oToi):
    lReturn = []
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        add_index_constraint_open_parenthesis(oToken, lReturn)
        add_index_constraint_close_parenthesis(oToken, lReturn)
        add_first_open_parenthesis(oToken, lReturn)
        add_last_close_parenthesis(oToken, lReturn)
    return lReturn


def add_index_constraint_open_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.index_constraint.open_parenthesis)


def add_index_constraint_close_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.index_constraint.close_parenthesis)


def add_first_open_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.procedure_call.open_parenthesis)


def add_last_close_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.procedure_call.close_parenthesis)


def add_token_type(oToken, lReturn, oTokenType):
    if isinstance(oToken, oTokenType):
        lReturn.append(oTokenType())
