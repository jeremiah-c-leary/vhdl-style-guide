
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.designator)


class rule_501(token_case_with_prefix_suffix):
    '''
    This rule checks the procedure designator has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       procedure AVERAGE_SAMPLES is

    **Fix**

    .. code-block:: vhdl

       procedure average_samples is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'procedure', '501', lTokens)
        self.groups.append('case::name')
