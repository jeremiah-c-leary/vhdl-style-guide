
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import case_statement as token


class rule_010(blank_line_below_line_ending_with_token):
    '''
    Case rule 010 ensures a blank line exists below the "end case" keywords.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'case', '010', [token.semicolon])
