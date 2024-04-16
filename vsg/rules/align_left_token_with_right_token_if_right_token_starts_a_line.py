# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import alignment
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class align_left_token_with_right_token_if_right_token_starts_a_line(alignment.Rule):
    """
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region
    """

    def __init__(self, left_token, right_token):
        super().__init__()
        self.left_token = left_token
        self.right_token = right_token
        self.configuration.append("align_to")
        self.align_to = "keyword"
        self.configuration_documentation_link = "configuring_keyword_alignment_rules_link"

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        lReturn = []
        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if not utils.does_token_start_line(len(lTokens) - 1, lTokens):
                continue

            oToi.set_meta_data("iRightColumn", oFile.get_column_of_token_index(oToi.get_start_index()))
            oToi.set_meta_data("indentLevel", oFile.get_indent_of_line_at_index(oToi.get_start_index()))
            lReturn.append(oToi)

        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            sActualWhitespace = extract_whitespace_before_last_token(oToi)
            sExpectedWhitespace = expected_whitespace_before_last_token(self, oToi)

            if sActualWhitespace != sExpectedWhitespace:
                oViolation = create_violation(oToi, sActualWhitespace, sExpectedWhitespace)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction["action"] == "insert":
            rules_utils.insert_new_whitespace(lTokens, len(lTokens) - 1, dAction["whitespace"])
        else:
            lTokens[-2].set_value(dAction["whitespace"])
        oViolation.set_tokens(lTokens)


def create_violation(oToi, sActualWhitespace, sExpectedWhitespace):
    iLine, lTokens = utils.get_toi_parameters(oToi)
    iLineNumber = iLine + utils.count_token_types_in_list_of_tokens(parser.carriage_return, lTokens)
    sSolution = "Align " + lTokens[-1].get_value() + " with " + lTokens[0].get_value()
    dAction = {}
    if sActualWhitespace == "":
        dAction["action"] = "insert"
    else:
        dAction["action"] = "adjust"
    dAction["whitespace"] = sExpectedWhitespace
    oViolation = violation.New(iLineNumber, oToi, sSolution)
    oViolation.set_action(dAction)
    return oViolation


def extract_whitespace_before_last_token(oToi):
    lTokens = oToi.get_tokens()
    iWhitespaceIndex = len(lTokens) - 2
    if rules_utils.token_is_whitespace(lTokens[iWhitespaceIndex]):
        return lTokens[iWhitespaceIndex].get_value()
    return ""


def expected_whitespace_before_last_token(self, oToi):
    sReturn = indent_whitespace(self, oToi)
    if self.align_to == "keyword":
        sReturn += aligning_whitespace(self, oToi)
    return sReturn


def indent_whitespace(self, oToi):
    iIndentLevel = oToi.get_meta_data("indentLevel")
    if self.indent_style == "smart_tabs":
        return "\t" * iIndentLevel
    return " " * iIndentLevel * self.indent_size


def aligning_whitespace(self, oToi):
    iIndentLength = len(indent_whitespace(self, oToi))
    iRightColumn = oToi.get_meta_data("iRightColumn")
    return " " * (iRightColumn - iIndentLength)
