
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.entity_specification.colon)


class rule_100(single_space_after_token):
    '''
    Checks for a single space after the colon
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'entity_specification', '100', lTokens)
