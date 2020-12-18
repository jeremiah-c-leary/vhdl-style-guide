
from vsg import rule
from vsg import violation


class remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region
    '''

    def __init__(self, name, identifier, left_token, right_token):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.left_token = left_token
        self.right_token = right_token

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.left_token, self.right_token, include_trailing_whitespace=True)

    def _analyze(self, lToi):
        for oToi in lToi:
           self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        oViolation.set_tokens([])
