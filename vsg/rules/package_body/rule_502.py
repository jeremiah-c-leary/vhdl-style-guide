
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_body.package_simple_name)


class rule_502(token_case_with_prefix_suffix):
    '''
    This rule checks the package name has proper case in the package declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package body FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       package body fifo_pkg is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package_body', '502', lTokens)
        self.groups.append('case::name')
