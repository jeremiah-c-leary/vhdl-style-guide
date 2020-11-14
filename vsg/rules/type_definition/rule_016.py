
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.enumeration_type_definition.close_parenthesis)


class rule_016(token_indent):
    '''
    Checks for the proper indentation of the closing parenthesis if it is on it's own line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'type', '016', lTokens)
