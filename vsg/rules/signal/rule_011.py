
from vsg import token

from vsg.rules import token_case_subtype_indication

lStartTokens = []
lStartTokens.append(token.signal_declaration.colon)

lEndTokens = []
lEndTokens.append(token.signal_declaration.assignment_operator)
lEndTokens.append(token.signal_declaration.semicolon)
lEndTokens.append(token.signal_kind.register_keyword)
lEndTokens.append(token.signal_kind.bus_keyword)


class rule_011(token_case_subtype_indication):
    '''
    Checks the signal type has proper case.
    '''

    def __init__(self):
        token_case_subtype_indication.__init__(self, 'signal', '011', lStartTokens, lEndTokens)
