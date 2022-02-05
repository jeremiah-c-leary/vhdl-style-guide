
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.end_case_keyword)


class rule_018(token_case):
    '''
    This rule checks the **case** keyword has proper case in the **end case**.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

          end CASE;
          end CAse;
          end case;

    **Fix**

    .. code-block:: vhdl

          end case;
          end case;
          end case;
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '018', lTokens)
        self.groups.append('case::keyword')
