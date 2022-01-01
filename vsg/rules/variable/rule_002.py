
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.variable_keyword)


class rule_002(token_case):
    '''
    This rule checks the **variable** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       VARIABLE count : integer;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;
    '''

    def __init__(self):
        token_case.__init__(self, 'variable', '002', lTokens)
        self.groups.append('case::keyword')
