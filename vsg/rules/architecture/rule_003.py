
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import architecture_body as token


class rule_003(blank_line_above_line_starting_with_token):
    '''
    Architecture rule 003 checks for a blank line above the architecture keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'architecture', '003', [token.architecture_keyword])
        self.method = 'require_blank'
