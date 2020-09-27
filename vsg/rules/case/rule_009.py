
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import case_statement as token


class rule_009(blank_line_above_line_starting_with_token):
    '''
    Case rule 009 ensures a blank line exists above the "end case" keywords.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'case', '009', [token.end_keyword])
