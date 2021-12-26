
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffix on variable identifiers.
    The default variable suffix is *\_v*.

    Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

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
