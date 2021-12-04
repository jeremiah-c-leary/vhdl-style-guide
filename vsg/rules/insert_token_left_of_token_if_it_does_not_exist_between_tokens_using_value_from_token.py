

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils

from vsg.rules import utils as rules_utils


class insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token(rule.Rule):
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
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
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
            check_for_existence_of_optional_keyword(lToi, self)
        else:
            check_for_missing_optional_keyword(lToi, self)

    def _fix_violation(self, oViolation):
        if remove_keyword(self):
            lTokens = oViolation.get_tokens()
            rules_utils.remove_optional_item(oViolation, self.insert_token)
        else:
            add_optional_item(oViolation, self)


def remove_keyword(self):
    if self.action == 'remove':
        return True
    return False


def check_for_existence_of_optional_keyword(lToi, self):
    for oToi in lToi:
        sSolution = self.action.capitalize() + ' ' + self.solution
        self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))


def check_for_missing_optional_keyword(lToi, self):
    for oToi in lToi:
        iLine, lTokens = utils.get_toi_parameters(oToi)
        bFound = False
        for oToken in lTokens:
           iLine = utils.increment_line_number(iLine, oToken)
           if isinstance(oToken, self.insert_token):
               bFound = True
               break
        if not bFound:
            sSolution = self.action.capitalize() + ' ' + self.solution
            self.add_violation(violation.New(iLine, oToi, sSolution))


def add_optional_item(oViolation, self):
    lTokens = oViolation.get_tokens()
    if oViolation.get_token_value() is not None:
        for iIndex in range(0, len(lTokens)):
            if isinstance(lTokens[iIndex], self.anchor_token):
                rules_utils.insert_token(lTokens, iIndex, self.insert_token(oViolation.get_token_value()))
                if not isinstance(lTokens[iIndex - 1], parser.whitespace):                
                    rules_utils.insert_whitespace(lTokens, iIndex)
        oViolation.set_tokens(lTokens)
