
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_012(token_prefix):
    '''
    This rule checks for valid prefixes on variable identifiers.
    The default variable prefix is *v\_*.

    Refer to `Configuring Prefix and Suffix Rules <configuring_prefix_and_suffix_rules.html>`_ for information on changing the allowed prefixes.

    **Violation**

    .. code-block:: vhdl

       variable my_var : natural;

    **Fix**

    .. code-block:: vhdl

       variable v_my_var : natural;
    '''

    def __init__(self):
        token_prefix.__init__(self, 'variable', '012', lTokens)
        self.prefixes = ['v_']
        self.solution = 'Variable identifiers'
