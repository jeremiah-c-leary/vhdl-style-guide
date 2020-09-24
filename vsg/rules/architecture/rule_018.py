
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import architecture_body as token


class rule_018(blank_line_above_line_starting_with_token):
    '''
    Architecture rule 018 checks for a blank line above the *end* keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'architecture', '018', [token.end_keyword])
