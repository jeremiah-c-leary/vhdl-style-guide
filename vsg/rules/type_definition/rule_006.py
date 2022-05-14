
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.full_type_declaration.identifier, token.full_type_declaration.is_keyword])


class rule_006(Rule):
    '''
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       type state_machine    is (idle, write, read, done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
    '''
    def __init__(self):
        Rule.__init__(self, 'type', '006', lTokens)
