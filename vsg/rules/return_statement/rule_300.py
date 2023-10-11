
from vsg.rules import token_indent as Rule

from vsg import token

lTokens = []
lTokens.append(token.return_statement.return_keyword)


class rule_300(Rule):
    '''
    This rule checks the indentation of the **return** keyword.

    **Violation**

    .. code-block:: vhdl

         return my_value;
         end function;

    **Fix**

    .. code-block:: vhdl

           return my_value;
         end function;
    '''

    def __init__(self):
        Rule.__init__(self, 'return_statement', '300', lTokens)
