
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.mode.in_keyword)
lTokens.append(token.mode.out_keyword)
lTokens.append(token.mode.inout_keyword)
lTokens.append(token.mode.buffer_keyword)
lTokens.append(token.mode.linkage_keyword)

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_019(token_case_in_range_bounded_by_tokens):
    '''
    Checks the "port" keyword has proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'port', '019', lTokens, oStart, oEnd)
