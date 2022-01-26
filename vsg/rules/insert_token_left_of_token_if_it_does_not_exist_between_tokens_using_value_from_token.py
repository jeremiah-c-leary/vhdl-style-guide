

from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils


class insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token(structure.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object
       token to check if insert_token exists to the right of

    value_token : token object
       token to pull the value from
    '''

    def __init__(self, name, identifier, insert_token, anchor_token, left_token, right_token, value_token):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.left_token = left_token
        self.right_token = right_token
        self.value_token = value_token
        self.action = 'add'
        self.configuration.append('action')

    def _get_tokens_of_interest(self, oFile):
        if remove_keyword(self):
            return oFile.get_token_and_n_tokens_before_it([self.insert_token], 1)
        else:
            return oFile.get_tokens_between_tokens_inclusive_while_storing_value_from_token(self.left_token, self.right_token, self.value_token)

    def _analyze(self, lToi):
        if remove_keyword(self):
            analyze_for_existence_of_optional_keyword(lToi, self)
        else:
            analyze_for_missing_optional_keyword(lToi, self)

    def _fix_violation(self, oViolation):
        if remove_keyword(self):
            rules_utils.remove_optional_item(oViolation, self.insert_token)
        else:
            add_optional_item(oViolation, self)


def remove_keyword(self):
    if self.action == 'remove':
        return True
    return False


def analyze_for_existence_of_optional_keyword(lToi, self):
    for oToi in lToi:
        oViolation = create_violation(oToi, oToi.get_line_number(), self)
        self.add_violation(oViolation)


def analyze_for_missing_optional_keyword(lToi, self):
    for oToi in lToi:
        iLine, lTokens = utils.get_toi_parameters(oToi)
        if not optional_keyword_exists(self.insert_token, lTokens):
            iLine += rules_utils.get_number_of_carriage_returns_before_token(self.anchor_token, lTokens)
            oViolation = create_violation(oToi, iLine, self)
            self.add_violation(oViolation)


def optional_keyword_exists(oToken, lTokens):
    if rules_utils.get_index_of_token_in_list(oToken, lTokens) is None:
        return False
    return True


def add_optional_item(oViolation, self):
    lTokens = oViolation.get_tokens()
    if not token_value_available(oViolation):
        return

    if not optional_keyword_exists(self.anchor_token, lTokens):
        return

    iIndex = rules_utils.get_index_of_token_in_list(self.anchor_token, lTokens)

    rules_utils.insert_token(lTokens, iIndex, self.insert_token(oViolation.get_token_value()))
    if not rules_utils.whitespace_before_token_index(lTokens, iIndex):
        rules_utils.insert_whitespace(lTokens, iIndex)
    oViolation.set_tokens(lTokens)


def token_value_available(oViolation):
    if oViolation.get_token_value() is not None:
        return True
    return False


def create_violation(oToi, iLineNumber, self):
    sSolution = self.action.capitalize() + ' ' + self.solution
    oViolation = violation.New(iLineNumber, oToi, sSolution)
    return oViolation
