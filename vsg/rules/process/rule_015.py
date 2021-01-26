
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_keyword)
lTokens.append(token.process_statement.process_label)


class rule_015(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the "process" keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'process', '015', lTokens)
        self.style = 'no_code'
