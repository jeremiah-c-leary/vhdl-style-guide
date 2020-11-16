
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generate_statement_body.end_keyword)


class rule_018(token_indent):
    '''
    Checks the indent of the generate label.
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '018', lTokens)
