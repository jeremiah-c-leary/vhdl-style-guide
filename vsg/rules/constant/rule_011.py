
from vsg import token

from vsg.rules import token_case_subtype_indication

lStartTokens = []
lStartTokens.append(token.constant_declaration.colon)

lEndTokens = []
lEndTokens.append(token.constant_declaration.assignment_operator)
lEndTokens.append(token.constant_declaration.semicolon)


class rule_011(token_case_subtype_indication):
    '''
    This rule checks the constant type has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       constant size : INTEGER := 1;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
    '''

    def __init__(self):
        token_case_subtype_indication.__init__(self, 'constant', '011', lStartTokens, lEndTokens)
        self.groups.append('case::name')
