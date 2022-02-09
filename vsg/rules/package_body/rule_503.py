
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_body.is_keyword)


class rule_503(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package fifo_pkg IS

    **Fix**

    .. code-block:: vhdl

       package fifo_pkg is
    '''

    def __init__(self):
        token_case.__init__(self, 'package_body', '503', lTokens)
        self.groups.append('case::keyword')
