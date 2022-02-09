
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_kind.function_keyword)


class rule_014(token_case):
    '''
    This rule checks the **function** keyword in the **end function** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end FUNCTION;

       end Function foo;

    **Fix**

    .. code-block:: vhdl

       end function;

       end function foo;
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '014', lTokens)
        self.groups.append('case::keyword')
