
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import architecture_body as token


class rule_016(blank_line_above_line_starting_with_token):
    '''
    Architecture rule 016 checks for a blank line above the "begin" keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'architecture', '016', [token.begin_keyword])
