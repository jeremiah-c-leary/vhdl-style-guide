
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of the package declaration.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         package FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       package FIFO_PKG is
    '''

    def __init__(self):
        token_indent.__init__(self, 'package', '001', lTokens)
