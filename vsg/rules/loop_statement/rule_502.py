
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.end_loop_keyword)


class rule_502(Rule):
    '''
    This rule checks the **loop** keyword has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       while (condition) loop

       end LOOP;

    **Fix**

    .. code-block:: vhdl

       while (condition) loop

       end loop;
    '''

    def __init__(self):
        Rule.__init__(self, 'loop_statement', '502', lTokens)
        self.groups.append('case::keyword')
