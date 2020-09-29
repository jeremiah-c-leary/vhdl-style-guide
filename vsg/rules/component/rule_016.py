
from vsg.rules import remove_blank_lines_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_016(remove_blank_lines_above_line_starting_with_token):
    '''
    Component rule 016 checks for a blank line above the "end component" keywords.
    '''

    def __init__(self):
        remove_blank_lines_above_line_starting_with_token.__init__(self, 'component', '016', lTokens)
