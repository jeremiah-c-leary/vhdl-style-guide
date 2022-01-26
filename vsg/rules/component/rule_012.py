
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.component_simple_name)


class rule_012(token_case_with_prefix_suffix):
    '''
    This rule checks the proper case of the component name in the **end component** line.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end component FIFO;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'component', '012', lTokens)
        self.groups.append('case::name')
