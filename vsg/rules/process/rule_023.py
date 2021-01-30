
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_keyword)


class rule_023(previous_line):
    '''
    Checks for a blank line above the "end process" keywords.
    '''

    def __init__(self):
        previous_line.__init__(self, 'process', '023', lTokens)
