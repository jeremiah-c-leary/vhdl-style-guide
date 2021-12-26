
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.end_entity_keyword)


class rule_014(token_case):
    '''
    This rule checks the **entity** keyword has proper case in the closing of the entity declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end ENTITY fifo;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '014', lTokens)
        self.groups.append('case::keyword')
