
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_014(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       End;

       END context;

    **Fix**

    .. code-block:: vhdl

       end;

       end context;
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '014', lTokens)
        self.groups.append('case::keyword')
