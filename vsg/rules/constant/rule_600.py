
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffixes on constant identifiers.
    The default constant suffix is *\_c*.

    Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

    **Violation**

    .. code-block:: vhdl

       constant my_const : integer;

    **Fix**

    .. code-block:: vhdl

       constant my_const_c : integer;
    '''

    def __init__(self):
        token_suffix.__init__(self, 'constant', '600', lTokens)
        self.suffixes = ['_c']
