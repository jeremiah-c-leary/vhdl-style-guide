
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import component_declaration as token


class rule_018(blank_line_below_line_ending_with_token):
    '''
    Component rule 018 checks for a blank line below the
    "end component" keywords.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'component', '018', [token.semicolon])
