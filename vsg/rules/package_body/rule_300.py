
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.package_body.package_keyword)


class rule_300(token_indent):
    '''
    This rule checks the indent of the package body keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         package body FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       package body FIFO_PKG is
    '''

    def __init__(self):
        token_indent.__init__(self, 'package_body', '300', lTokens)
