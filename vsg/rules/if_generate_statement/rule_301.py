
from vsg.rules import token_indent as Rule

from vsg import token

lTokens = []
lTokens.append(token.if_generate_statement.else_keyword)


class rule_301(Rule):
    '''
    This rule checks the indent of the *else* keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : if condition generate
          else
       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : if condition generate
       else
       end generate;
    '''

    def __init__(self):
        Rule.__init__(self, 'if_generate_statement', '301', lTokens)
