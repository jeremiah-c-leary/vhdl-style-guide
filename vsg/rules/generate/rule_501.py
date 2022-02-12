
from vsg import token

from vsg.rules import token_case

lTokens = []
lTokens.append(token.generate_statement_body.end_keyword)


class rule_501(token_case):
    '''
    This rule checks the **end** keyword has the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       for condition generate
         begin
         END
       end generate;

    **Fix**

    .. code-block:: vhdl

       for condition generate
         begin
         end
       end generate;
    '''

    def __init__(self):
        token_case.__init__(self, 'generate', '501', lTokens)
        self.groups.append('case::keyword')
