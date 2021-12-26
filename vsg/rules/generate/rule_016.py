
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.case_generate_alternative.when_keyword)


class rule_016(token_indent):
    '''
    This rule checks the indent of the **when** keyword in generate case statements.

    **Violation**

    .. code-block:: vhdl

       GEN_LABEL : case condition generate
         when 0 =>
           when 1 =>
       when 2 =>

    **Fix**

    .. code-block:: vhdl

       GEN_LABEL : case condition generate
         when 0 =>
         when 1 =>
         when 2 =>
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '016', lTokens)
