
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.signal_declaration.colon, parser.todo])


class rule_005(single_space_between_token_pairs):
    '''
    Checks for a single space after the :.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'signal', '005', lTokens)
        self.solution = 'Ensure only a signal space after the colon.'
