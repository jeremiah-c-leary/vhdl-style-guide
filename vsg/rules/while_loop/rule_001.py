
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)
lTokens.append(token.iteration_scheme.while_keyword)


class rule_001(token_indent):
    '''
    For loop rule 001 checks while the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'while_loop', '001', lTokens)
