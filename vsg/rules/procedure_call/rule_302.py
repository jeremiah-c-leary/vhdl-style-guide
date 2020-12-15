
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.procedure_call.procedure_name)


class rule_302(token_indent):
    '''
    Checks for indent of the procedure name.
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure_call', '302', lTokens)
