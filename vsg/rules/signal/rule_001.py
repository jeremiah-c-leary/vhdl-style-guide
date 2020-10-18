
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.signal_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the signal statement.
    '''

    def __init__(self):
        token_indent.__init__(self, 'signal', '001', lTokens)
