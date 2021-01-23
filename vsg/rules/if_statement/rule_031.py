
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.if_keyword)


class rule_031(blank_line_above_line_starting_with_token):
    '''
    Ensures a blank line exists above the if label.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'if', '031', lTokens)
        self.lHierarchyLimits = [0]
        self.method = 'no_code'
