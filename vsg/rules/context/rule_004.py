
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.context_keyword)


class rule_004(token_case):
    '''
    This rule checks the **context** keyword has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       CONTEXT c1 is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '004', lTokens)
        self.groups.append('case::keyword')
