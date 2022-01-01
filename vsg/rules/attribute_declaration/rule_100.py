
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.attribute_declaration.attribute_keyword)
lTokens.append(token.attribute_declaration.colon)


class rule_100(single_space_after_token):
    '''
    This rule checks for a single space after the following elements:  **attribute** keyword and colon.

    **Violation**

    .. code-block:: vhdl

       attribute   max_delay :   time;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'attribute_declaration', '100', lTokens)
