
from vsg.rules import token_indent as Rule

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.end_keyword)
lTokens.append(token.for_generate_statement.end_keyword)
lTokens.append(token.if_generate_statement.end_keyword)


class rule_300(Rule):
    '''
    This rule checks the indent of the end keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
          end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       end generate;
    '''

    def __init__(self):
        Rule.__init__(self, 'generate', '300', lTokens)
