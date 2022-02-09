
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_context_keyword)


class rule_015(token_case):
    '''
    This rule checks the context keyword has proper case in the end context declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end CONTEXT;

    **Fix**

    .. code-block:: vhdl

       end context;
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '015', lTokens)
        self.groups.append('case::keyword')
