
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generate_statement_body.begin_keyword)


class rule_006(token_indent):
    '''
    Checks the indent of the begin keyword in the generate_statement_body.
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '006', lTokens)
