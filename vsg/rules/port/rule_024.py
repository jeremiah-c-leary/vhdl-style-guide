
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import port_clause as token

lTokens = []
lTokens.append(token.close_parenthesis)

class rule_024(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks blank lines above the closing parenthesis.
    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'port', '024', lTokens, iAllow=0)
        self.solution = 'Remove blank lines above ).'
