
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.if_statement.if_keyword)


class rule_031(previous_line):
    '''
    Ensures a blank line exists above the if label.
    '''

    def __init__(self):
        previous_line.__init__(self, 'if', '031', lTokens)
        self.lHierarchyLimits = [0]
        self.style = 'no_code'
