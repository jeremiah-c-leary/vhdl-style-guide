
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.label_name)
lTokens.append(token.procedure_call_statement.label)


class rule_300(token_indent):
    '''
    Checks for indent of the block label.
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure_call', '300', lTokens)
