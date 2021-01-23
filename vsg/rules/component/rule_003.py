
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import component_declaration as token


class rule_003(blank_line_above_line_starting_with_token):
    '''
    Component rule 003 checks for a blank line above the component keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'component', '003', [token.component_keyword])
        self.method = 'no_code'
