
from vsg.rules import token_case as Rule

from vsg.token import predefined_attribute as token

lTokens = []
lTokens.append(token.keyword)


class rule_500(Rule):
    '''
    This rule checks predefined attributes have the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal data : std_logic_vector(g_width'RANGE);

    **Fix**

    .. code-block:: vhdl

       signal data : std_logic_vector(g_width'range);
    '''

    def __init__(self):
        Rule.__init__(self, 'attribute', '500', lTokens)
        self.groups.append('case::keyword')
