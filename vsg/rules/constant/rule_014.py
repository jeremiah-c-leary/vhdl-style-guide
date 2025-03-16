# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import (
    alignment_utils,
    multiline_alignment_between_tokens as Rule,
    utils as rules_utils,
)
from vsg.vhdlFile import utils

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.assignment_operator, token.constant_declaration.semicolon])


class rule_014(Rule):
    """
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
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.subphase = 3
        self.phase = 5
        self.iIndentAfterParen = 0

    def _get_tokens_of_interest(self, oFile):
        for lTokenPair in self.lTokenPairs:
            lToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = remove_arrays(lToi)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            oToi.set_meta_data("oFirstLineIndentToken", alignment_utils.get_first_line_indent_token(iLine, oFile))
            oToi.set_meta_data("iAssignColumn", oFile.get_column_of_token_index(oToi.get_start_index(), self.indent_size))

        return lToi


def remove_arrays(lToi):
    lReturn = []
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if not rules_utils.token_list_starts_with_paren(lTokens, 1):
            lReturn.append(oToi)
    return lReturn


def _get_indent_of_line(iLine, oFile):
    lTemp = oFile.get_tokens_from_line(iLine)
    oToken = lTemp.get_tokens()[0]

    if isinstance(oToken, parser.whitespace):
        oToken = lTemp.get_tokens()[1]
        return oToken.indent
    else:
        oToken = lTemp.get_tokens()[0]
        return oToken.indent
