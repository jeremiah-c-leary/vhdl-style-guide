
from vsg.rules import token_indent as Rule

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.begin_keyword)


class rule_300(Rule):
    '''
    This rule checks the indent of the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is

            begin

    **Fix**

    .. code-block:: vhdl

       entity FIFO is

       begin
    '''

    def __init__(self):
        Rule.__init__(self, 'entity', '300', lTokens)
