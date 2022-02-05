
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_body_keyword)


class rule_506(token_case):
    '''
    This rule checks the **body** keyword in the **end package body** has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end package BODY fifo_pkg;

    **Fix**

    .. code-block:: vhdl

       end package body fifo_pkg;
    '''

    def __init__(self):
        token_case.__init__(self, 'package_body', '506', lTokens)
        self.groups.append('case::keyword')
