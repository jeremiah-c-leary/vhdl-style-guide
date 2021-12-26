
from vsg.rules import split_line_at_token_when_between_tokens_unless_token_is_found

from vsg import token

lTokens = []
lTokens.append(token.assertion.report_keyword)

oStart = token.assertion.keyword
oEnd = token.assertion_statement.semicolon
oStop = token.concurrent_assertion_statement.semicolon


class rule_003(split_line_at_token_when_between_tokens_unless_token_is_found):
    '''
    This rule checks the **report** keyword is on its own line for sequential assertion statements.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin

         process
         begin

           assert WIDTH > 16 report "FIFO width is limited to 16 bits."
             severity FAILURE;

         end process;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin

         process
         begin

           assert WIDTH > 16
             report "FIFO width is limited to 16 bits."
             severity FAILURE;

         end process;

       end architecture rtl;
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens_unless_token_is_found.__init__(self, 'assert', '003', lTokens, oStart, oEnd, oStop)
        self.solution = "Place **report** keyword on its own line."
