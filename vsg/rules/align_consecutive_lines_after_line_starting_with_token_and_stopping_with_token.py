# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import alignment
from vsg.rules import alignment_utils, utils as rules_utils


class align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token(alignment.Rule):
    """ """

    def __init__(self):
        super().__init__()
        self.alignment = "report"
        self.configuration.append("alignment")
        self.phase = 4
        self.lStartTokens = []
        self.lEndTokens = []
        self.indentAdjust = 1

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(self.lStartTokens, self.lEndTokens, True, False, True)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            lIndexes = get_index_after_carriage_return(lTokens)

            for iIndex in lIndexes:
                myToi = oToi.extract_tokens(iIndex, iIndex)
                myToi.set_meta_data("iSpaces", self._calculate_column(oFile, oToi, lTokens))
                myToi.set_meta_data("sWhitespace", self._expected_whitespace(oFile, oToi, lTokens))
                lReturn.append(myToi)

        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            self._check_leading_whitespace(oToi)

    def _check_leading_whitespace(self, oToi):
        sWhitespace = oToi.get_meta_data("sWhitespace")
        oToken = oToi.get_tokens()[0]
        if isinstance(oToken, parser.whitespace):
            if oToken.get_value() != sWhitespace:
                self._create_violation(oToi, "adjust")
        else:
            self._create_violation(oToi, "insert")

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        if dAction["action"] == "adjust":
            lTokens[0].set_value(dAction["whitespace"])
        else:
            rules_utils.insert_new_whitespace(lTokens, 0, dAction["whitespace"])

        oViolation.set_tokens(lTokens)

    def _create_violation(self, oToi, sAction):
        sSolution = alignment_utils.build_solution(oToi.get_meta_data("sWhitespace"))
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        dAction = {}
        dAction["action"] = sAction
        dAction["column"] = oToi.get_meta_data("iSpaces")
        dAction["whitespace"] = oToi.get_meta_data("sWhitespace")
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

    def _calculate_column(self, oFile, oToi, lTokens):
        if self.alignment == "report":
            iSpaces = oFile.get_column_of_token_index(oToi.get_start_index()) + 7
        else:
            iSpaces = (lTokens[0].indent + self.indentAdjust) * self.indent_size
        return iSpaces

    def _expected_whitespace(self, oFile, oToi, lTokens):
        if self.indent_style == "smart_tabs":
            if self.alignment == "report":
                return (lTokens[0].indent) * "\t" + " " * (len(lTokens[0].get_value()) + 1)
            else:
                return (lTokens[0].indent + self.indentAdjust) * "\t"
        else:
            if self.alignment == "report":
                iSpaces = oFile.get_column_of_token_index(oToi.get_start_index()) + (len(lTokens[0].get_value()) + 1)
            else:
                iSpaces = (lTokens[0].indent + self.indentAdjust) * self.indent_size
            return iSpaces * " "


def get_index_after_carriage_return(lTokens):
    lReturn = []
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, parser.carriage_return):
            lReturn.append(iToken + 1)
    return lReturn
