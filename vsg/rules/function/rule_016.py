
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.return_statement.return_keyword)


class rule_016(token_indent):
    '''
    This rule checks the indent of return statements in function bodies.

    **Violation**

    .. code-block:: vhdl

       function func1 return integer is
       begin
            return 99;
       return 99;
       end func1;

    **Fix**

    .. code-block:: vhdl

       function func1 return integer is
       begin
         return 99;
         return 99;
       end func1;
    '''

    def __init__(self):
        token_indent.__init__(self, 'function', '016', lTokens)
