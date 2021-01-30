
from vsg import token

from vsg.rules import previous_line

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_010(previous_line):
    '''
    Checks for a blank line above the "type" declaration.
    '''

    def __init__(self):
        previous_line.__init__(self, 'type', '010', lTokens)
