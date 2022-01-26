
from vsg import parser
from vsg import violation

from vsg.rule_group import whitespace
from vsg.rules import utils as rules_utils


class whitespace_before_tokens_in_between_tokens(whitespace.Rule):
    '''
    Checks for at least a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token object types
       reference token to check for a whitespace before

    oStart : token object type
       The beginning of the range

    oEnd : token object type
       The end of the range
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_token_and_n_tokens_before_it_in_between_tokens(self.lTokens, 1, self.oStart, self.oEnd)

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
