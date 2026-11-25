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
            ],
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

            if block_rule.style_can_autofix_separator(oToken, dStyle, "footer_string", "footer_left", "footer_left_repeat"):
                oViolation.set_action({"expected": sFooter})

            self.add_violation(oViolation)


def select_autofix_footer_style_index(self, oToi):
    lComments = block_rule.get_comment_tokens(oToi)
    oFooterToken = lComments[-1] if lComments else None
    return block_rule.select_autofix_style_index(self, oToi, oFooterToken, "footer_string", "footer_left", "footer_left_repeat")
