
from vsg import token

from vsg.rules import whitespace_before_tokens_in_between_tokens

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_file_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_014(whitespace_before_tokens_in_between_tokens):
    '''
    Constant rule 014 checks for at least a single space before the := keyword.
    '''
    def __init__(self):
        whitespace_before_tokens_in_between_tokens.__init__(self, 'generic', '014', lTokens, oStart, oEnd)
        self.solution = 'Add a space before the :.'
