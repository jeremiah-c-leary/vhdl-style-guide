# -*- coding: utf-8 -*-

from vsg import block_rule, parser, violation
from vsg.vhdlFile import utils


class rule_003(block_rule.Rule):
    """
    This rule checks the block comment footer is correct.

    |configuring_block_comments_link|

    **Violation**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --|  Comment
       --|  Comment
       ----------------------------------------

    **Fix**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --|  Comment
       --|  Comment
       --+--------------------------[ Footer ]=
    """

    def __init__(self):
        super().__init__()
        self.fixable = True
        self.configuration.extend(
            [
                "footer_left",
                "footer_left_repeat",
                "footer_string",
                "footer_right_repeat",
                "footer_alignment",
                "max_footer_column",
            ]
        )

    def analyze_comments(self, oToi):
        iLine, lTokens = utils.get_toi_parameters(oToi)
        iComments = utils.count_token_types_in_list_of_tokens(parser.comment, lTokens)

        iStyleIndex = select_autofix_footer_style_index(self, oToi)
        dStyle = self.get_style(iStyleIndex)

        iComment = 0
        for oToken in lTokens:
            iLine = utils.increment_line_number(iLine, oToken)
            iComment = utils.increment_comment_counter(iComment, oToken)

            if last_comment(iComment, iComments):
                analyze_footer(self, oToken, iLine, oToi, dStyle)

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction is None or "expected" not in dAction:
            return

        lTokens = oViolation.get_tokens()

        for oToken in reversed(lTokens):
            if isinstance(oToken, parser.comment):
                oToken.set_value(dAction["expected"])
                break

        oViolation.set_tokens(lTokens)


def last_comment(iComment, iComments):
    return iComment == iComments


def analyze_footer(self, oToken, iLine, oToi, dStyle):
    sFooter = self.build_footer(oToken, dStyle)
    sComment = oToken.get_value()

    if block_rule.is_footer(sComment):
        self.set_token_indent(oToken)
        if sComment != sFooter:
            sSolution = "Change block comment footer to : " + sFooter
            oViolation = violation.New(iLine, oToi, sSolution)

            if style_can_autofix_separator_footer(oToken, dStyle):
                oViolation.set_action({"expected": sFooter})

            self.add_violation(oViolation)


def select_autofix_footer_style_index(self, oToi):
    lComments = block_rule.get_comment_tokens(oToi)
    if not lComments:
        return self.select_style_index(oToi)

    oFooterToken = lComments[-1]

    for iStyleIndex in range(self.get_style_count()):
        dStyle = self.get_style(iStyleIndex)
        if style_can_autofix_separator_footer(oFooterToken, dStyle):
            return iStyleIndex

    return self.select_style_index(oToi)


def style_can_autofix_separator_footer(oToken, dStyle):
    sComment = oToken.get_value()

    if dStyle["footer_string"] not in (None, ""):
        return False

    sPrefix = "--"
    if dStyle["footer_left"] is not None:
        sPrefix += dStyle["footer_left"]

    sRepeat = dStyle["footer_left_repeat"] or ""
    if sRepeat == "":
        return False

    if not sComment.startswith(sPrefix):
        return False

    sTail = sComment[len(sPrefix) :]
    if sTail == "":
        return True

    for sChar in sTail:
        if sChar != sRepeat:
            return False

    return True
