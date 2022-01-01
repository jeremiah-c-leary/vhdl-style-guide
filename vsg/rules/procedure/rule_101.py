
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_kind.procedure_keyword])
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_body.designator])
lTokens.append([token.subprogram_kind.procedure_keyword, token.subprogram_body.designator])

class rule_101(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the **end** and **procedure** keywords and procedure designator.

    **Violation**

    .. code-block:: vhdl

       end   procedure   average_samples;
       end   procedure;
       end   average_samples;

    **Fix**

    .. code-block:: vhdl

       end procedure average_samples;
       end procedure;
       end average_samples;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'procedure', '101', lTokens)
        self.solution = 'Ensure a single space between the keywords in the closing part of a procedure specification.'

