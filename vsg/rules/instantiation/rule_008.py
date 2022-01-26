
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_008(token_case_with_prefix_suffix):
    '''
    This rule checks the instance label has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : fifo

    **Fix**

    .. code-block:: vhdl

       u_fifo : fifo
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'instantiation', '008', lTokens)
        self.groups.append('case::label')
