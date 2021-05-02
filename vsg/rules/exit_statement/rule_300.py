
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.exit_statement.label)
lTokens.append(token.exit_statement.exit_keyword)


class rule_300(token_indent):
    '''
    Checks for indent of the exit_statement label.
    '''

    def __init__(self):
        token_indent.__init__(self, 'exit_statement', '300', lTokens)
