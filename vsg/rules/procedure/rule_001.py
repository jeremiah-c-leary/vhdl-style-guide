
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.procedure_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the procedure specification.
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure', '001', lTokens)
