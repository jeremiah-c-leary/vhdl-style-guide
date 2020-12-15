
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.postponed_keyword)


class rule_301(token_indent):
    '''
    Checks for indent of the postponed keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure_call', '301', lTokens)
