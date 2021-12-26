
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.end_keyword)


class rule_028(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       END if;

       End if;

    **Fix**

    .. code-block:: vhdl

       end if;

       end if;
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '028', lTokens)
        self.groups.append('case::keyword')
