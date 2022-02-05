
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_004(token_case):
    '''
    This rule checks the package keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       PACKAGE FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       package FIFO_PKG is
    '''

    def __init__(self):
        token_case.__init__(self, 'package', '004', lTokens)
        self.groups.append('case::keyword')
