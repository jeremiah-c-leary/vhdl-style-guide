
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.end_keyword)


class rule_501(Rule):
    '''
    This rule checks the **end** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       while (condition) loop

       END loop;

    **Fix**

    .. code-block:: vhdl

       while (condition) loop

       end loop;
    '''

    def __init__(self):
        Rule.__init__(self, 'loop_statement', '501', lTokens)
        self.groups.append('case::keyword')
