
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)


class rule_412(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    This rule checks for alignment of inline comments for each parameter in the procedure declaration.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

         procedure average_samples (
           constant a : in integer;   -- Comment about a
           signal d   : out std_logic;   -- Comment about d
         );

    **Fix**

    .. code-block:: vhdl

         procedure average_samples (
           constant a : in integer;    -- Comment about a
           signal d   : out std_logic; -- Comment about d
         );
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(
            self, 'procedure', '412', lAlign,
            token.procedure_specification.open_parenthesis, token.procedure_specification.close_parenthesis, lSkip)
        self.solution = 'Align comment.'
        self.subphase = 3
