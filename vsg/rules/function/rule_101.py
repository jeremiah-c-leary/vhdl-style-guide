
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_kind.function_keyword])
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_body.designator])
lTokens.append([token.subprogram_kind.function_keyword, token.subprogram_body.designator])


class rule_101(Rule):
    '''
    This rule checks for a single space between the **end** and **function** keywords and function designator.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'function', '101', lTokens)
