
from vsg import token

from vsg.rules import token_case_subtype_indication

lStartTokens = []
lStartTokens.append(token.constant_declaration.colon)

lEndTokens = []
lEndTokens.append(token.constant_declaration.assignment_operator)
lEndTokens.append(token.constant_declaration.semicolon)


class rule_011(token_case_subtype_indication):
    '''
    Checks the constant type has proper case.
    '''

    def __init__(self):
        token_case_subtype_indication.__init__(self, 'constant', '011', lStartTokens, lEndTokens)
