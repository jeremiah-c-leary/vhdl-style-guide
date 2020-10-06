
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import generic_clause as token

lTokens = []
lTokens.append(token.close_parenthesis)

class rule_019(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for blank lines above the closing parenthesis.
    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'generic', '019', lTokens, iAllow=0)
