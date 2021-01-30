
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_004(previous_line):
    '''
    Ensures a blank line exists above the instantiation label.
    '''

    def __init__(self):
        previous_line.__init__(self, 'instantiation', '004', lTokens)
        self.style = 'no_code'
