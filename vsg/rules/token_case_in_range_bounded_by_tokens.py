
from vsg import rules


class token_case_in_range_bounded_by_tokens(rules.token_case):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types

    oStart : token type

    oEnd : token type
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rules.token_case.__init__(self, name=name, identifier=identifier, lTokens=lTokens)
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)
