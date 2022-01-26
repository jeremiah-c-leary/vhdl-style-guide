
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_package_keyword)


class rule_505(token_case):
    '''
    This rule checks the **package** keyword in the **end package body** has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end PACKAGE body fifo_pkg;

    **Fix**

    .. code-block:: vhdl

       end package body fifo_pkg;
    '''

    def __init__(self):
        token_case.__init__(self, 'package_body', '505', lTokens)
        self.groups.append('case::keyword')
