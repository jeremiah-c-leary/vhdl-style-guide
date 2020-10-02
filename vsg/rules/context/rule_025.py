
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import context_declaration as token


class rule_025(blank_line_below_line_ending_with_token):
    '''
    Case rule 025 ensures a blank line exists below the semicolon.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'context', '025', [token.semicolon])
