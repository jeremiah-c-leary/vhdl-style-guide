

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils


class insert_token_right_of_token_if_it_does_not_exist(rule.Rule):
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
    '''

    def __init__(self, name, identifier, insert_token, anchor_token):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.action = 'add'
        self.configuration.append('action')

    def _get_tokens_of_interest(self, oFile):
        if self.action == 'add':
            return oFile.get_sequence_of_tokens_not_matching([self.anchor_token, parser.whitespace, type(self.insert_token)])
        else:
            return oFile.get_token_and_n_tokens_before_it([self.insert_token], 1)

    def _analyze(self, lToi):
        for oToi in lToi:
            sSolution = self.action.capitalize() + ' ' + self.solution
            self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.action == 'add':
            utils.add_optional_item(lTokens, oViolation, self.insert_token)
        else:
            utils.remove_optional_item(lTokens, oViolation, self.insert_token)
