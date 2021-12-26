
from vsg import parser
from vsg import token

from vsg.rules import remove_lines_starting_with_token_between_token_pairs

lTokens = []
lTokens.append([token.simple_release_assignment.assignment, token.simple_release_assignment.semicolon])
lTokens.append([token.simple_force_assignment.assignment, token.simple_force_assignment.semicolon])
lTokens.append([token.simple_waveform_assignment.assignment, token.simple_waveform_assignment.semicolon])

oRemoveToken = parser.comment


class rule_006(remove_lines_starting_with_token_between_token_pairs):
    '''
    This rule checks for comments within multiline sequential statements.

    **Violation**

    .. code-block:: vhdl

       overflow <= wr_en and
        --         rd_address(0)
                   rd_en;

    **Fix**

    .. code-block:: vhdl

       overflow <= wr_en and
                   rd_en;
    '''

    def __init__(self):
        remove_lines_starting_with_token_between_token_pairs.__init__(self, 'sequential', '006', oRemoveToken, lTokens)
        self.solution = 'Remove comments inside sequential assignment'
        self.fixable = False
