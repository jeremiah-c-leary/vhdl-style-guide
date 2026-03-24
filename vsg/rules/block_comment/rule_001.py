# -*- coding: utf-8 -*-

from vsg import block_rule, parser, violation


class rule_001(block_rule.Rule):
    """
    This rule checks the block comment header is correct.

    |configuring_block_comments_link|

    **Violation**

    .. code-block:: vhdl

       ----------------------------------------
       --   Comment
       --   Comment
       ----------------------------------------

    **Fix**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --   Comment
       --   Comment
       ----------------------------------------
    """

    def __init__(self):
        super().__init__()
        self.fixable = True
        self.configuration.extend(
            [
                "header_left",
                "header_left_repeat",
                "header_string",
                "header_right_repeat",
                "header_alignment",
                "max_header_column",
            ]
        )

    def analyze_comments(self, oToi):
        oToken = oToi.get_first_token_matching(parser.comment)
        if oToken is None:
            return

        sComment = oToken.get_value()

        try:
            if not block_rule.is_header(sComment):
                return
        except IndexError:
            return

        self.set_token_indent(oToken)

        iStyleIndex = select_autofix_header_style_index(self, oToi)
        dStyle = self.get_style(iStyleIndex)
        sHeader = self.build_header(oToken, dStyle)

        if sComment != sHeader:
            sSolution = "Change block comment header to : " + sHeader
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)

            if style_can_autofix_separator_header(oToken, dStyle):
                oViolation.set_action({"expected": sHeader})

            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction is None or "expected" not in dAction:
            return

        lTokens = oViolation.get_tokens()

        for oToken in lTokens:
            if isinstance(oToken, parser.comment):
                oToken.set_value(dAction["expected"])
                break

        oViolation.set_tokens(lTokens)


def select_autofix_header_style_index(self, oToi):
    oHeaderToken = oToi.get_first_token_matching(parser.comment)
    if oHeaderToken is None:
        return self.select_style_index(oToi)

    for iStyleIndex in range(self.get_style_count()):
        dStyle = self.get_style(iStyleIndex)
        if style_can_autofix_separator_header(oHeaderToken, dStyle):
            return iStyleIndex

    return self.select_style_index(oToi)


def style_can_autofix_separator_header(oToken, dStyle):
    sComment = oToken.get_value()

    if dStyle["header_string"] not in (None, ""):
        return False

    sPrefix = "--"
    if dStyle["header_left"] is not None:
        sPrefix += dStyle["header_left"]

    sRepeat = dStyle["header_left_repeat"] or ""
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


#         1         2         3         4         5         6         7         8
# -------------------------------<-    80 chars    ->-----------------------------
# ------------------------------<-    80 chars    ->------------------------------
