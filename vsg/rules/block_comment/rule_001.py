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
            ],
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

            if block_rule.style_can_autofix_separator(oToken, dStyle, "header_string", "header_left", "header_left_repeat"):
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
    return block_rule.select_autofix_style_index(self, oToi, oHeaderToken, "header_string", "header_left", "header_left_repeat")


#         1         2         3         4         5         6         7         8
# -------------------------------<-    80 chars    ->-----------------------------
# ------------------------------<-    80 chars    ->------------------------------
