
from vsg.rules import token_indent as Rule


class token_indent_between_tokens(Rule):
    '''
    Checks the indent of tokens.
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd, bInclusive=False):
        Rule.__init__(self, name=name, identifier=identifier, lTokens=lTokens)
        self.oStart = oStart
        self.oEnd = oEnd
        self.bInclusive = bInclusive

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_at_beginning_of_line_matching_between_tokens(self.lTokens, self.oStart, self.oEnd, self.bInclusive)
