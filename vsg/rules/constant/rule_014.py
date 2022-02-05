
from vsg.rules import multiline_alignment_between_tokens as Rule

from vsg import parser
from vsg import token
from vsg.vhdlFile import utils
from vsg.rules import utils as rules_utils

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.assignment_operator, token.constant_declaration.semicolon])


class rule_014(Rule):
    '''
    This rule checks the indent of multiline constants that do not contain arrays.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant width : integer := a + b +
         c + d;

    **Fix**

    .. code-block:: vhdl

       constant width : integer := a + b +
                                   c + d;
    '''

    def __init__(self):
        Rule.__init__(self, 'constant', '014', lTokenPairs)
        self.subphase = 3
        self.phase = 5

    def _get_tokens_of_interest(self, oFile):
        for lTokenPair in self.lTokenPairs:
            lToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = remove_arrays(lToi)
        return lToi


def remove_arrays(lToi):
    lReturn = []
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if not rules_utils.token_list_starts_with_paren(lTokens, 1):
            lReturn.append(oToi)
    return lReturn
