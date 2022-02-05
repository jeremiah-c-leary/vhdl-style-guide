
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.end_keyword)


class rule_017(token_case):
    '''
    This rule checks the **end** keyword in the **end case** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

          End case;
          END case;
          end case;

    **Fix**

    .. code-block:: vhdl

          end case;
          end case;
          end case;
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '017', lTokens)
        self.groups.append('case::keyword')
