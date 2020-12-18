
from vsg import rule
from vsg import parser
from vsg import violation


class split_line_at_token(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object type to split a line at
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_token_and_n_tokens_before_it(self.lTokens, 2)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if isinstance(lTokens[0], parser.carriage_return) or isinstance(lTokens[1], parser.carriage_return):
                continue
            sSolution = self.solution
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[1], parser.whitespace):
            lTokens.insert(-2, parser.carriage_return())
        else:
            lTokens.insert(-1, parser.carriage_return())
        oViolation.set_tokens(lTokens)
