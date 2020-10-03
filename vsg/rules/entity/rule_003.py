
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import entity_declaration as token


class rule_003(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the "entity" keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'entity', '003', [token.entity_keyword])
