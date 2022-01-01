
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.function_specification.designator)


class rule_017(token_case):
    '''
    This rule checks the function designator has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       function OVERflow (a: integer) return integer is

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '017', lTokens)
        self.groups.append('case::name')
