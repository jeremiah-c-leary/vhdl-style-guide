
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.semicolon)
lTokens.append(token.for_generate_statement.semicolon)
lTokens.append(token.if_generate_statement.semicolon)


class rule_003(blank_line_below_line_ending_with_token):
    '''
    Ensures a blank line exists below the semicolon.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'generate', '003', lTokens)
