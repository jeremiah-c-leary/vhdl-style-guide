
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_keyword)


class rule_300(token_indent):
    '''
    For loop rule 300 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'loop_statement', '300', lTokens)
