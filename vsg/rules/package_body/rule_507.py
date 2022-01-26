
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_package_simple_name)


class rule_507(token_case_with_prefix_suffix):
    '''
    This rule checks the package name has proper case on the end package declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end package body FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package fifo_pkg;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package_body', '507', lTokens)
        self.groups.append('case::name')
