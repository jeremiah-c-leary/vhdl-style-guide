
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import architecture_body as token


class rule_015(blank_line_below_line_ending_with_token):
    '''
    Architecture rule 015 checks for a blank line below the *is* keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'architecture', '015', [token.is_keyword])
