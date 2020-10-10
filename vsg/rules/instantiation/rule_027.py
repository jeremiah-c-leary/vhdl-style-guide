
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.entity_keyword)


class rule_027(token_case):
    '''
    Checks the **entity** keyword has proper case in direct instantiations.
    '''

    def __init__(self):
        token_case.__init__(self, 'instantiation', '027', lTokens)
