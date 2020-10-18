
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.variable_assignment_statement.label)
lTokens.append(token.simple_variable_assignment.target)
lTokens.append(token.conditional_variable_assignment.target)
lTokens.append(token.selected_variable_assignment.with_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of a variable declaration.
    '''

    def __init__(self):
        token_indent.__init__(self, 'variable_assignment', '001', lTokens)
