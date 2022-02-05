
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.generic_clause.generic_keyword)


class rule_009(token_case):
    '''
    This rule checks the **generic** keyword has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       GENERIC (

    **Fix**

    .. code-block:: vhdl

       generic (
    '''

    def __init__(self):
        token_case.__init__(self, 'generic', '009', lTokens)
        self.groups.append('case::keyword')
