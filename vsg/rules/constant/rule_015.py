
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_015(token_prefix):
    '''
    This rule checks for valid prefixes on constant identifiers.
    The default constant prefix is *c\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant my_const : integer;

    **Fix**

    .. code-block:: vhdl

       constant c_my_const : integer;
    '''

    def __init__(self):
        token_prefix.__init__(self, 'constant', '015', lTokens)
        self.prefixes = ['c_']
