
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.then_keyword)


class rule_029(token_case):
    '''
    This rule checks the **then** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       if (a = '1') THEN

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '029', lTokens)
        self.groups.append('case::keyword')
