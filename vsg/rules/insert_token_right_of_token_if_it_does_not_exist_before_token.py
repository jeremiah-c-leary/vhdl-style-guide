
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils


class insert_token_right_of_token_if_it_does_not_exist_before_token(rule.Rule):
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

    anchor_token : token object type
       token to check if insert_token exists to the right of

    end_token : token object type
       token that bounds the search for the insert_token
    '''

    def __init__(self, name, identifier, insert_token, anchor_token, end_token):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.end_token = end_token
        self.action = 'add'
        self.configuration.append('action')

    def _get_tokens_of_interest(self, oFile):
        if self.action == 'add':
            return oFile.get_tokens_bounded_by(self.anchor_token, self.end_token)
        else:
            return oFile.get_token_and_n_tokens_before_it([self.insert_token], 1)

    def _analyze(self, lToi):
        if self.action == 'remove':
            for oToi in lToi:
                sSolution = self.action.capitalize() + ' ' + self.solution
                self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
            return

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bFound = False
            for oToken in lTokens:
                if isinstance(oToken, type(self.insert_token)):
                    bFound = True
                    break
            if not bFound:
                sSolution = self.action.capitalize() + ' ' + self.solution
                self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.action == 'remove':
            rules_utils.remove_optional_item(lTokens, oViolation, self.insert_token)
        else:
            rules_utils.insert_token(lTokens, 1, self.insert_token)
            rules_utils.insert_whitespace(lTokens, 1)
            oViolation.set_tokens(lTokens)
