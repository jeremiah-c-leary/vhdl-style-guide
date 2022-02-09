
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_kind.procedure_keyword)


class rule_009(token_case):
    '''
    This rule checks the **procedure** keyword in the **end procedure** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end PROCEDURE;

       end Procedure proc;

    **Fix**

    .. code-block:: vhdl

       end procedure;

       end procedure proc;
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '009', lTokens)
        self.groups.append('case::keyword')
