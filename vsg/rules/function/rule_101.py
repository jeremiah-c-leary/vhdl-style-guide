
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_kind.function_keyword])
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_body.designator])
lTokens.append([token.subprogram_kind.function_keyword, token.subprogram_body.designator])


class rule_101(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the **end** and **function** keywords and function designator.

    **Violation**

    .. code-block:: vhdl

       end   function   overflow;
       end   function;
       end   overflow;

    **Fix**

    .. code-block:: vhdl

       end function overflow;
       end function;
       end overflow;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'function', '101', lTokens)
        self.solution = 'Ensure a single space between the keywords in the closing part of a function specification.'

