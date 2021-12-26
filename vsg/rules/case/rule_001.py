
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.case_statement.case_keyword)
lTokens.append(token.case_statement.end_keyword)
lTokens.append(token.case_statement_alternative.when_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of **case**, **when**, and **end case** keywords.

    **Violation**

    .. code-block:: vhdl


       case data is

           when 0 =>
       when 1 =>
               when 3 =>

      end case;

    **Fix**

    .. code-block:: vhdl

      case data is

        when 0 =>
        when 1 =>
        when 3 =>

      end case;
    '''

    def __init__(self):
        token_indent.__init__(self, 'case', '001', lTokens)
