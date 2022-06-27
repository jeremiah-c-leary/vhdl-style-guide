
from vsg import rules
from vsg.rules import utils


class token_case_in_range_bounded_by_tokens_with_prefix_suffix(rules.token_case_with_prefix_suffix):
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
        rules.token_case_with_prefix_suffix.__init__(self, name=name, identifier=identifier, lTokens=lTokens)
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        self.case_exceptions_lower = utils.lowercase_list(self.case_exceptions)
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)
