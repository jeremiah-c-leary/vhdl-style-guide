
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_process_keyword)


class rule_009(token_case):
    '''
    This rule checks the **process** keyword has proper case in the **end process** line.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end PROCESS proc_a;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    '''

    def __init__(self):
        token_case.__init__(self, 'process', '009', lTokens)
        self.groups.append('case::keyword')
