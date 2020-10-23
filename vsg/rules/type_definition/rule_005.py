
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)


class rule_005(token_indent):
    '''
    Checks for the proper indentation of multiline enumerated types.
    '''

    def __init__(self):
        token_indent.__init__(self, 'type', '005', lTokens)
        self.solution = 'Ensure proper indentation.'
