
from vsg import token

from vsg.rules import blank_line_above_line_starting_with_token

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_010(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the "type" declaration.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'type', '010', lTokens)
