
from vsg import token

from vsg.rules import token_case

lTokens = []
lTokens.append(token.generate_statement_body.begin_keyword)


class rule_500(token_case):
    '''
    This rule checks the **begin** keyword has the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       for condition generate
         BEGIN

    **Fix**

    .. code-block:: vhdl

       for condition generate
         begin
    '''

    def __init__(self):
        token_case.__init__(self, 'generate', '500', lTokens)
        self.groups.append('case::keyword')
