
from vsg.rules import utils as rules_utils
from vsg.rules import create_violation


def add_new_line_and_remove_new_line(self, oToi, sOption, oTokenType):
    if sOption == 'ignore':
        return
    elif sOption == 'add_new_line':
        rules_utils.analyze_with_function(self, oToi, oTokenType, analyze_add_new_line)
    elif sOption == 'remove_new_line':
        rules_utils.analyze_with_function(self, oToi, oTokenType, analyze_remove_new_line)


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
