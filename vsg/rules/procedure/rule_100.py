
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.procedure_specification.procedure_keyword, token.procedure_specification.designator])
lTokens.append([token.procedure_specification.designator, token.subprogram_body.is_keyword])
lTokens.append([token.procedure_specification.designator, token.procedure_specification.open_parenthesis])
lTokens.append([token.procedure_specification.close_parenthesis, token.subprogram_body.is_keyword])

class rule_100(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the following procedure elements:  **procedure** keyword, procedure designator, open parenthesis, close parenthesis, and **is** keywords.

    **Violation**

    .. code-block:: vhdl

       procedure    average_samples    (
           constant a : in integer;
           signal d : out std_logic
         )    is
       procedure    average_samples      is

    **Fix**

    .. code-block:: vhdl

       procedure average_samples (
           constant a : in integer;
           signal d : out std_logic
         ) is
       procedure average_samples is
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'procedure', '100', lTokens)
        self.solution = 'Ensure a single space between the keywords in the opening part of a procedure specification.'

