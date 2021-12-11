
from vsg import rules


class token_case_subtype_indication(rules.token_case):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types
       The token types to check the case one.

    lEndTokens: list of token types
       The token types to stop searching.
    '''

    def __init__(self, name, identifier, lTokens, lEndTokens):
        rules.token_case.__init__(self, name=name, identifier=identifier, lTokens=lTokens)
        self.lEndTokens = lEndTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(self.lTokens, self.lEndTokens)
