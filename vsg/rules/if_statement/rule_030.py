
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.semicolon)


class rule_030(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line after the "end if" keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'if', '030', lTokens)
        self.lHierarchyLimits = [0]
