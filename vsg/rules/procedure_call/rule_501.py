
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.postponed_keyword)


class rule_501(token_case):
    '''
    This rule checks the **postponed** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       POSTPONED WR_EN(parameter)

    **Fix**

    .. code-block:: vhdl

       postponed WR_EN(parameter)
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure_call', '501', lTokens)
        self.groups.append('case::keyword')
