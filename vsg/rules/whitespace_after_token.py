
from vsg.rules import utils

from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule


class Rule(WhitespaceRule):
    '''
    Checks for a single space after a token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token type object list
       A list of tokens to check for a single space after.
    '''

    def __init__(self, name, identifier, lTokens):
        WhitespaceRule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_token_and_n_tokens_after_it(self.lTokens, 2)
        lToi = utils.remove_toi_if_token_is_at_the_end_of_the_line(lToi)
        return lToi
