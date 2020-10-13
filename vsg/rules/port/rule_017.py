
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.port_clause.port_keyword)


class rule_017(token_case):
    '''
    Checks the "port" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'port', '017', lTokens)
