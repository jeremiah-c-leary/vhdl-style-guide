
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.is_keyword)


class rule_006(token_case):
    '''
    This rule checks the **is** keyword has proper case in the entity declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       entity fifo IS

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '006', lTokens)
        self.groups.append('case::keyword')
