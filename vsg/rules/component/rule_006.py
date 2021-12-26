
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.is_keyword)


class rule_006(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       component fifo IS

       component fifo Is

    **Fix**

    .. code-block:: vhdl

       component fifo is

       component fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '006', lTokens)
        self.groups.append('case::keyword')
