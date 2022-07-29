
from vsg import token

from vsg.rules import utils as rules_utils
from vsg.rules import check
from vsg.rules import create_violation
from vsg.rules import fix
from vsg.rules import tokens_of_interest as toi

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
        self.exceptions = []
        self.configuration.append('exceptions')

    def _get_tokens_of_interest(self, oFile):
        return toi.get_tokens_bounded_by(self.lTokenPairs, oFile)

    def _analyze(self, lToi):
        for oToi in lToi:

            if exception_applied(self, oToi):
                continue

            _check_record_constraint_open_paren(self, oToi)
            _check_record_constraint_close_paren(self, oToi)
            _check_record_constraint_comma(self, oToi)
            _check_record_constraint_element(self, oToi)
            _check_array_constraint(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        fix.fix_violation(oViolation)


def _check_array_constraint(self, oToi):

    if self.array_constraint == 'ignore':
        return
    elif self.array_constraint == 'all_in_one_line':
        analyze_array_constraint_with_function(self, oToi, analyze_for_array_constraint_all_in_one_line)
    elif self.array_constraint == 'one_line_per_dimension':
        analyze_array_constraint_with_function(self, oToi, analyze_for_array_constraint_one_line_per_dimension)


def analyze_for_array_constraint_all_in_one_line(self, oToi):
    iStart = oToi.get_meta_data('iStart')
    iToken = oToi.get_meta_data('iToken')
    lTokens = oToi.get_tokens()

    if rules_utils.token_at_beginning_of_line_in_token_list(iStart, lTokens):
        oViolation = create_array_constraint_all_in_one_line_violation(oToi)
        self.add_violation(oViolation)
    elif rules_utils.number_of_carriage_returns(lTokens[iStart:iToken]) > 0:
        oViolation = create_array_constraint_remove_carriage_return_violation(oToi)
        self.add_violation(oViolation)


def create_array_constraint_all_in_one_line_violation(oToi):
    oToi.set_meta_data('sSolution', 'Move open parenthesis to previous line and remove carriage returns in array constraint.')
    oToi.set_meta_data('sAction', 'remove_new_line')
    toi.adjust_start_index_based_on_whitespace(oToi, -2)
    oViolation = create_violation._create_violation(oToi)
    return oViolation


def analyze_array_constraint_with_function(self, oToi, fFunction):
    iLine, lTokens = rules_utils.get_toi_parameters(oToi)
    oStartToken = token.index_constraint.open_parenthesis
    oEndToken = token.index_constraint.close_parenthesis

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, oStartToken):
            oToi.set_meta_data('iStart', iToken)
            oToi.set_meta_data('iStartLine', iLine)
        if isinstance(oToken, oEndToken):
            oToi.set_meta_data('iToken', iToken)
            fFunction(self, oToi)


def analyze_for_array_constraint_one_line_per_dimension(self, oToi):
    iStart = oToi.get_meta_data('iStart')
    iToken = oToi.get_meta_data('iToken')
    lTokens = oToi.get_tokens()
    if not rules_utils.token_at_beginning_of_line_in_token_list(iStart, lTokens):
        oViolation = create_array_constraint_one_line_violation(oToi)
        self.add_violation(oViolation)
    elif rules_utils.number_of_carriage_returns(lTokens[iStart:iToken]) > 0:
        oViolation = create_array_constraint_remove_carriage_return_violation(oToi)
        self.add_violation(oViolation)


def create_array_constraint_one_line_violation(oToi):
    iStart = oToi.get_meta_data('iStart')
    lTokens = oToi.get_tokens()
    oToi.set_meta_data('sSolution', 'Move open parenthesis to next line and remove carriage returns in array constraint.')
    oToi.set_meta_data('sAction', 'add_new_line_and_remove_carraige_returns')
    toi.adjust_start_index_based_on_whitespace(oToi, -1)
    oViolation = create_violation._create_violation(oToi)
    return oViolation


def create_array_constraint_remove_carriage_return_violation(oToi):
    oToi.set_meta_data('sSolution', 'Remove carriage returns in array constraint.')
    oToi.set_meta_data('sAction', 'remove_new_line')
    oViolation = create_violation._create_violation(oToi)
    return oViolation


def _check_record_constraint_open_paren(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.record_constraint_open_paren, token.record_constraint.open_parenthesis)


def _check_record_constraint_close_paren(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.record_constraint_close_paren, token.record_constraint.close_parenthesis)


def _check_record_constraint_comma(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.record_constraint_comma, token.record_constraint.comma)


def _check_record_constraint_element(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.record_constraint_element, token.record_element_constraint.record_element_simple_name)


def exception_applied(self, oToi):
    if _check_for_exception_one(self, oToi):
        return True
    return False


def _check_for_exception_one(self, oToi):
    if not exception_enabled(self):
        return False
    if not token_pattern_match(oToi):
        return False
    analyze_exception_one(self, oToi)
    return True


def exception_enabled(self):
    if 'keep_record_constraint_with_single_element_on_one_line' in self.exceptions:
        return True
    return False


def analyze_exception_one(self, oToi):
    iLine, lTokens = rules_utils.get_toi_parameters(oToi)
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        oToi.set_meta_data('iToken', iToken)
        record_constraint_open_paren_detected(oToi, iLine, oToken)
        record_constraint_close_paren_detected(self, oToi, oToken)


def record_constraint_open_paren_detected(oToi, iLine, oToken):
    if isinstance(oToken, token.record_constraint.open_parenthesis):
        oToi.set_meta_data('iStart', oToi.get_meta_data('iToken'))
        oToi.set_meta_data('iStartLine', iLine)


def record_constraint_close_paren_detected(self, oToi, oToken):
    if isinstance(oToken, token.record_constraint.close_parenthesis):
        lTokens = oToi.get_tokens()
        iStart = oToi.get_meta_data('iStart')
        iToken = oToi.get_meta_data('iToken')
        if rules_utils.number_of_carriage_returns(lTokens[iStart:iToken]) > 0:
            oViolation = create_array_constraint_remove_carriage_return_violation(oToi)
            self.add_violation(oViolation)


def token_pattern_match(oToi):
    lActual = filter_tokens(oToi)
    lExpected = create_expected_token_pattern()
    if len(lExpected) != len(lActual):
        return False
    for iIndex in range(0, len(lExpected)):
        if not isinstance(lActual[iIndex], lExpected[iIndex]):
            return False
    return True


def create_expected_token_pattern():
    lCheckType = []
    lCheckType.append(token.record_constraint.open_parenthesis)
    lCheckType.append(token.index_constraint.open_parenthesis)
    lCheckType.append(token.index_constraint.close_parenthesis)
    lCheckType.append(token.record_constraint.close_parenthesis)
    return lCheckType


def filter_tokens(oToi):
    lReturn = []
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        add_index_constraint_open_parenthesis(oToken, lReturn)
        add_index_constraint_close_parenthesis(oToken, lReturn)
        add_record_constraint_open_parenthesis(oToken, lReturn)
        add_record_constraint_close_parenthesis(oToken, lReturn)
    return lReturn


def add_index_constraint_open_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.index_constraint.open_parenthesis)


def add_index_constraint_close_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.index_constraint.close_parenthesis)


def add_record_constraint_open_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.record_constraint.open_parenthesis)


def add_record_constraint_close_parenthesis(oToken, lReturn):
    add_token_type(oToken, lReturn, token.record_constraint.close_parenthesis)


def add_token_type(oToken, lReturn, oTokenType):
    if isinstance(oToken, oTokenType):
        lReturn.append(oTokenType())
