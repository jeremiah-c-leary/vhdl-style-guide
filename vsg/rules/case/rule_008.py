
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import case_statement as token


class rule_008(blank_line_below_line_ending_with_token):
    '''
    Case rule 008 ensures a blank line exists below the "case" keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'case', '008', [token.is_keyword])
