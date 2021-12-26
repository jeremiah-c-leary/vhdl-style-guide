
from vsg.rules import token_case_with_prefix_suffix

from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.entity_name)


class rule_014(token_case_with_prefix_suffix):
    '''
    This rule checks the case of the entity name in the architecture declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of FIFO is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'architecture', '014', lTokens)
        self.groups.append('case::name')
