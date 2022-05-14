
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.procedure_specification.procedure_keyword, token.procedure_specification.designator])
lTokens.append([token.procedure_specification.designator, token.subprogram_body.is_keyword])
lTokens.append([token.procedure_specification.designator, token.procedure_specification.open_parenthesis])
lTokens.append([token.procedure_specification.close_parenthesis, token.subprogram_body.is_keyword])

class rule_100(Rule):
    '''
    This rule checks for a single space between the following procedure elements:  **procedure** keyword, procedure designator, open parenthesis, close parenthesis, and **is** keywords.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'procedure', '100', lTokens)
