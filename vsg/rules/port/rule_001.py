
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import port_clause as token

lTokens = []
lTokens.append(token.port_keyword)

class rule_001(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for more than one blank line above the *port* keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'port', '001', lTokens, iAllow=0)
        self.solution = 'Remove blank lines above "port" keyword.'
