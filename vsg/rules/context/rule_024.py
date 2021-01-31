
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import context_declaration as token


class rule_024(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the end context declaration.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'context', '024', [token.end_keyword])
