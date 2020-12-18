
from vsg import parser
from vsg import rule
from vsg import violation


class remove_token_and_whitespace_before_it(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object type list
       tokens to remove

    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_token_and_n_tokens_before_it([self.lTokens[0]], 1)

    def _analyze(self, lToi):
        for oToi in lToi:
           self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[0], parser.whitespace):
            oViolation.set_tokens([])
        else:
            oViolation.set_tokens(lTokens[1])
