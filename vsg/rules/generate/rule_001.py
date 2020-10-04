
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_001(token_indent):
    '''
    Checks the indent of the generate label.
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '001', lTokens)
