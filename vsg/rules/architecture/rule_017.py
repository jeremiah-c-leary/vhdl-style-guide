
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import architecture_body as token


class rule_017(blank_line_below_line_ending_with_token):
    '''
    Architecture rule 017 checks for a blank line below the "begin" keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'architecture', '017', [token.begin_keyword])
