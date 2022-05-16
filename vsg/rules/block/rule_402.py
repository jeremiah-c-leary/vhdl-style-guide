
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.entity_specification.colon)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_402(Rule):
    '''
    This rule checks the colons are in the same column for all attribute specifications.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

         attribute mark_debug of wr_en : signal is "true";
         attribute mark_debug of almost_empty : signal is "true";
         attribute mark_debug of full : signal is "true";

    **Fix**

    .. code-block:: vhdl

         attribute mark_debug of wr_en        : signal is "true";
         attribute mark_debug of almost_empty : signal is "true";
         attribute mark_debug of full         : signal is "true";
    '''

    def __init__(self):
        Rule.__init__(self, 'block', '402', lAlign, token.block_statement.block_keyword, token.block_statement.begin_keyword, lUnless)
        self.solution = 'Align colon.'
