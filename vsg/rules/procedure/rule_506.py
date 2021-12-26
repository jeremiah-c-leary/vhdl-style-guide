
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)


class rule_506(token_case_with_prefix_suffix):
    '''
    This rule checks the procedure designator has proper case on the end procedure declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end procedure AVERAGE_SAMPLES;

    **Fix**

    .. code-block:: vhdl

       end procedure average_samples;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'procedure', '506', lTokens)
        self.groups.append('case::name')
