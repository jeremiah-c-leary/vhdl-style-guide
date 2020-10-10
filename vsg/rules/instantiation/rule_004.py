
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_004(blank_line_above_line_starting_with_token):
    '''
    Ensures a blank line exists above the instantiation label.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'instantiation', '004', lTokens)
