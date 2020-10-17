
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.postponed_keyword)
lTokens.append(token.process_statement.process_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the process specification.
    '''

    def __init__(self):
        token_indent.__init__(self, 'process', '001', lTokens)
