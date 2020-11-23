
from vsg.rules import split_line_at_token_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.generic_map_aspect.close_parenthesis)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_004(split_line_at_token_when_between_tokens):
    '''
    Checks the closing ) for the generic map is on it's own line.
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens.__init__(self, 'generic_map', '004', lTokens, oStart, oEnd)
        self.solution = 'Place closing ) on it\'s own line.'
