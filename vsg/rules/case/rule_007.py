
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import case_statement as token


class rule_007(blank_line_above_line_starting_with_token):
    '''
    Case rule 007 ensures a blank line exists before the "case" keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'case', '007', [token.case_keyword])
        self.style = 'no_code'
