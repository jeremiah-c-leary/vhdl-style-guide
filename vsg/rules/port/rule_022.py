
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg.token import port_clause as token

lTokens = []
lTokens.append(token.open_parenthesis)

class rule_022(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    Checks for more than one blank line above the *port* keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'port', '022', lTokens, iAllow=0)
        self.solution = 'Remove blank lines below *port* keyword.'
