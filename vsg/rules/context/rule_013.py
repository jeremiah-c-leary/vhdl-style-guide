
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.is_keyword)


class rule_013(token_case):
    '''
    This rule checks the **is** keyword has proper case in the context declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       context c1 IS

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '013', lTokens)
        self.groups.append('case::keyword')
