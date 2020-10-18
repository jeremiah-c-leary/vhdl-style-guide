
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.variable_declaration.colon, parser.todo])


class rule_005(single_space_between_token_pairs):
    '''
    Checks for a single space after the :.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'variable', '005', lTokens)
        self.solution = 'Ensure only a single space after the colon.'
