
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.procedure_keyword)


class rule_500(token_case):
    '''
    This rule checks the **procedure** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       PROCEDURE average_samples is

    **Fix**

    .. code-block:: vhdl

       procedure average_samples is
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '500', lTokens)
        self.groups.append('case::keyword')
