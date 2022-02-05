
from vsg import token

from vsg.rules import single_space_after_token as Rule

lTokens = []
lTokens.append(token.alias_declaration.is_keyword)


class rule_102(Rule):
    '''
    This rule checks for a single space after the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       alias alias_designator is     name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator is name;
    '''
    def __init__(self):
        Rule.__init__(self, 'alias_declaration', '102', lTokens)
