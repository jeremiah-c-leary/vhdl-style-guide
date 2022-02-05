
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_signal_declaration.colon)
lAlign.append(token.interface_constant_declaration.colon)
lAlign.append(token.interface_variable_declaration.colon)
lAlign.append(token.interface_unknown_declaration.colon)


class rule_410(align_tokens_in_region_between_tokens):
    '''
    This rule checks the alignment of the colon for each parameter in the procedure declaration.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

         procedure average_samples (
           constant a : in integer;
           signal d : out std_logic
         );

    **Fix**

    .. code-block:: vhdl

         procedure average_samples (
           constant a : in integer;
           signal d   : out std_logic
         );
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(
            self, 'procedure', '410', lAlign,
            token.procedure_specification.open_parenthesis, token.procedure_specification.close_parenthesis)
        self.solution = 'Align :.'
