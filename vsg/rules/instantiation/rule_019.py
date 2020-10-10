
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.semicolon)


class rule_019(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the end of the port map aspect.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'instantiation', '019', lTokens)
