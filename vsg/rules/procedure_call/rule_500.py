
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.label_name)
lTokens.append(token.procedure_call_statement.label)


class rule_500(token_case):
    '''
    This rule checks the label has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       PROCEDURE_CALL_LABEL : WR_EN(paremeter);

    **Fix**

    .. code-block:: vhdl

       procedure_call_label : WR_EN(paremeter);
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure_call', '500', lTokens)
        self.groups.append('case::label')
