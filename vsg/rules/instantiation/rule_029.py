
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)


class rule_029(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    This rule checks for alignment of inline comments in an instantiation.

    Following extra configurations are supported:

    * :code:`separate_generic_port_alignment`.

    |configuring_keyword_alignment_rules_link|
    **Violation**

    **Violation**

    .. code-block:: vhdl

           wr_en    => write_enable,        -- Wrte enable
           rd_en    => read_enable,    -- Read enable
           overflow => overflow,         -- FIFO has overflowed

    **Fix**

    .. code-block:: vhdl

           wr_en    => write_enable, -- Wrte enable
           rd_en    => read_enable,  -- Read enable
           overflow => overflow,     -- FIFO has overflowed
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'instantiation', '029', lAlign, token.component_instantiation_statement.instantiation_label, token.component_instantiation_statement.semicolon, lSkip)
        self.solution = 'Align comment.'
        self.subphase = 3
