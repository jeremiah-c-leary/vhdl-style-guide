
from vsg.rules import token_indent as Rule

from vsg import token

lTokens = []
lTokens.append(token.alias_declaration.alias_keyword)


class rule_300(Rule):
    '''
    This rule checks the indent of the **alias** keyword.

    **Violation**

    .. code-block:: vhdl

       signal sig1 : integer;

         alias is name;

    **Fix**

    .. code-block:: vhdl

       signal sig1 : integer;

       alias is name;
    '''

    def __init__(self):
        Rule.__init__(self, 'alias_declaration', '300', lTokens)
