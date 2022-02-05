
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffix on variable identifiers.
    The default variable suffix is *\_v*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable my_var : natural;

    **Fix**

    .. code-block:: vhdl

       variable my_var_v : natural;
    '''

    def __init__(self):
        token_suffix.__init__(self, 'variable', '600', lTokens)
        self.suffixes = ['_v']
        self.solution = 'Variable identifiers'
