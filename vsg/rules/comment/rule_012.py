# -*- coding: utf-8 -*-

from vsg import parser, severity, violation
from vsg.rule_group import structure


class rule_012(structure.Rule):
    """
    This rule checks for user defined keywords in comments.

    .. NOTE:: This rule is disabled by default.

    |configuring_comment_keywords_link|

    **Violation**

    .. code-block:: vhdl

       -- TODO:  Refactor the section below
       -- FIXME: Update

    **Fix**

    This is a reporting only rule.
    """

    def __init__(self):
        super().__init__()
        self.solution = "Move inline comment to previous line."
        self.disable = True
        self.fixable = False
        self.severity = severity.warning("Warning")
        self.keywords = ["TODO", "FIXME"]
        self.configuration.append("keywords")
        self.configuration_documentation_link = "configuring_comment_keywords_link"

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([parser.comment])

    def _analyze(self, lToi):
        for oToi in lToi:
            if self.comment_includes_keyword(oToi):
                self.create_violation(oToi)

    def comment_includes_keyword(self, oToi):
        sToken = oToi.get_tokens()[0].get_value()
        for sKeyword in self.keywords:
            if sKeyword in sToken:
                oToi.set_meta_data("keyword", sKeyword)
                return True
        return False

    def create_violation(self, oToi):
        sSolution = "Comment keyword " + oToi.get_meta_data("keyword") + " detected."
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        self.add_violation(oViolation)
