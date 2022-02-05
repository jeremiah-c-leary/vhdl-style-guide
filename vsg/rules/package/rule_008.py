
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_package_simple_name)


class rule_008(token_case_with_prefix_suffix):
    '''
    This rule checks the package name has proper case on the end package declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end package FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package fifo_pkg;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '008', lTokens)
        self.groups.append('case::name')
