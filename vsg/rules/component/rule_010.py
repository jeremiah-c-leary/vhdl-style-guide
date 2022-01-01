
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_010(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       END component fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '010', lTokens)
        self.groups.append('case::keyword')
