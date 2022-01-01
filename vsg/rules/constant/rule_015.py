
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_015(token_prefix):
    '''
    This rule checks for valid prefixes on constant identifiers.
    The default constant prefix is *c\_*.

    Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

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
