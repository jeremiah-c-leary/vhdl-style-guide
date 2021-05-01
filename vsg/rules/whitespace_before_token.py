

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils


class whitespace_before_token(rule.Rule):
    '''
    Checks for a at least a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object
       reference token check for a whitespace before
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_token_and_n_tokens_before_it(self.lTokens, 1)

    def _analyze(self, lToi):

        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if isinstance(lTokens[0], parser.whitespace):
                continue

            if isinstance(lTokens[0], parser.carriage_return):
                continue

            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.add_violation(oViolation)


    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        rules_utils.insert_whitespace(lTokens, 1)
        oViolation.set_tokens(lTokens)

