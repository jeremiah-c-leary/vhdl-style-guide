
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)


class rule_002(token_indent):
    '''
    Checks for the proper indentation at the beginning of the procedure specification.
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure', '002', lTokens)
