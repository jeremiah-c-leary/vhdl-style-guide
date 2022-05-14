
from vsg import parser
from vsg import violation

from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule
from vsg.rules import utils as rules_utils


class Rule(WhitespaceRule):
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
        WhitespaceRule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_token_and_n_tokens_before_it_in_between_tokens(self.lTokens, 2, self.oStart, self.oEnd)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if token_is_at_beginning_of_line(lTokens):
                continue
            if isinstance(lTokens[1], parser.whitespace):
                lReturn.append(oToi)
            else:
                lReturn.append(oToi.extract_tokens(1, 2))

        return lReturn


def token_is_at_beginning_of_line(lTokens):
    if isinstance(lTokens[0], parser.carriage_return):
        return True
    if isinstance(lTokens[1], parser.carriage_return):
        return True
    return False
