
from vsg.rules import blank_line_above_line_starting_with_token as rule


class Rule(rule):
    '''
    Checks for a blank line above a line starting with a given token when it is between tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line above should appear
    '''

    def __init__(self, name, identifier, lTokens, lAllowTokens=None):
        rule.__init__(self, name=name, identifier=identifier, lTokens=lTokens, lAllowTokens=lAllowTokens)
        self.lBetweenTokenPairs = None

    def _get_tokens_of_interest(self, oFile):
        if self.style == 'require_blank_line':
            return oFile.get_line_above_line_starting_with_token(self.lTokens, bIncludeComments=False)
        elif self.style == 'no_blank_line':
            return oFile.get_blank_lines_above_line_starting_with_token_when_between_tokens(self.lTokens, self.lBetweenTokenPairs)
