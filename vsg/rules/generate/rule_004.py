
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_004(blank_line_above_line_starting_with_token):
    '''
    Ensures a blank line exists above the generate label.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'generate', '004', lTokens)
