
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.process_statement.semicolon)


class rule_011(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the end process statment.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'process', '011', lTokens)
