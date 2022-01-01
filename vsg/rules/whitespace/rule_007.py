
from vsg import parser

from vsg.rules import n_spaces_after_tokens

lTokens = []
lTokens.append(parser.comma)


class rule_007(n_spaces_after_tokens):
    '''
    This rule checks for spaces after a comma.

    **Violation**

    .. code-block:: vhdl

       proc : process (wr_en,rd_en,overflow) is

    **Fix**

    .. code-block:: vhdl

       proc : process (wr_en, rd_en, overflow) is
    '''

    def __init__(self):
        n_spaces_after_tokens.__init__(self, 'whitespace', '007', 1, lTokens, bNIsMinimum=True)
        self.solution = 'Add a space after comma.'
