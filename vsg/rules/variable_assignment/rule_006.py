
from vsg import parser
from vsg import token

from vsg.rules import remove_lines_starting_with_token_between_token_pairs

lTokens = []
lTokens.append([token.simple_variable_assignment.target, token.simple_variable_assignment.semicolon])

oRemoveToken = parser.comment


class rule_006(remove_lines_starting_with_token_between_token_pairs):
    '''
    This rule checks for comments in multiline variable assignments.

    **Violation**

    .. code-block:: vhdl

         counter := 1 + 4 + 10 + 25 +
                    -- Add in more stuff
                    30 + 35;

    **Fix**

    .. code-block:: vhdl

         counter := 1 + 4 + 10 + 25 +
                    30 + 35;
    '''

    def __init__(self):
        remove_lines_starting_with_token_between_token_pairs.__init__(self, 'variable_assignment', '006', oRemoveToken, lTokens)
        self.solution = 'Remove comments inside variable assignment'
        self.fixable = False
