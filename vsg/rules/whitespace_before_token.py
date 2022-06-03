

from vsg import parser

from vsg.rules import utils as rules_utils

from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule


class Rule(WhitespaceRule):
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
        WhitespaceRule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_token_and_n_tokens_before_it(self.lTokens, 2)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if rules_utils.token_is_at_beginning_of_line(lTokens):
                continue
            lReturn.append(extract_toi(oToi))
        return lReturn


def extract_toi(oToi):
    lTokens = oToi.get_tokens()
    if isinstance(lTokens[1], parser.whitespace):
        return oToi
    else:
        return oToi.extract_tokens(1, 2)
