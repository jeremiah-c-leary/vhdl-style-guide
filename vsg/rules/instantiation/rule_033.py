
from vsg import parser
from vsg import token

from vsg.rules import remove_token_and_whitespace_before_it

lTokens = []
lTokens.append(token.instantiated_unit.component_keyword)


class rule_033(remove_token_and_whitespace_before_it):
    '''
    Removes the optional *component* keyword.
    '''
    def __init__(self):
        remove_token_and_whitespace_before_it.__init__(self, 'instantiation', '033', lTokens)
