
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.end_keyword)


class rule_002(token_indent):
    '''
    Checks for the proper indentation of the "end loop" keywords.
    '''

    def __init__(self):
        token_indent.__init__(self, 'while_loop', '002', lTokens)
