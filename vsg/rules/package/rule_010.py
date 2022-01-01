
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.identifier)


class rule_010(token_case_with_prefix_suffix):
    '''
    This rule checks the package name has proper case in the package declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       package FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       package fifo_pkg is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '010', lTokens)
        self.groups.append('case::name')
