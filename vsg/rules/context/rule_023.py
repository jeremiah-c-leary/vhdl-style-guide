
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import context_declaration as token


class rule_023(blank_line_below_line_ending_with_token):
    '''
    Case rule 023 ensures a blank line exists below the "is" keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'context', '023', [token.is_keyword])
