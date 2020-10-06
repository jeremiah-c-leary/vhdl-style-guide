
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs_bounded_by_tokens

lTokens = []
lTokens.append([token.interface_constant_declaration.assignment, parser.todo])
lTokens.append([token.interface_signal_declaration.assignment, parser.todo])
lTokens.append([token.interface_variable_declaration.assignment, parser.todo])
lTokens.append([token.interface_unknown_declaration.assignment, parser.todo])

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_006(single_space_between_token_pairs_bounded_by_tokens):
    '''
    Checks for a single space between the := and expression.
    '''
    def __init__(self):
        single_space_between_token_pairs_bounded_by_tokens.__init__(self, 'generic', '006', lTokens, oStart, oEnd)
        self.solution = 'Reduce number of spaces after the colon to 1.'
