
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.is_keyword)


class rule_013(token_case_with_prefix_suffix):
    '''
    This rule checks the **is** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       package fifo_pkg IS

    **Fix**

    .. code-block:: vhdl

       package fifo_pkg is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '013', lTokens)
        self.groups.append('case::keyword')
