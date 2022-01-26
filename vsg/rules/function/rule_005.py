
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.function_specification.function_keyword)


class rule_005(token_case):
    '''
    This rule checks the **function** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       FUNCTION overflow (a: integer) return integer is

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '005', lTokens)
        self.groups.append('case::keyword')
