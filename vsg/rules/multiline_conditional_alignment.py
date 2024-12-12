# -*- coding: utf-8 -*-

import copy

from vsg import parser, token, violation
from vsg.rule_group import alignment
from vsg.rules import alignment_utils, utils as rules_utils
from vsg.vhdlFile import utils


class multiline_conditional_alignment(alignment.Rule):
    """
    This rule checks alignment of multiline concurrent conditional signal statements.

    |configuring_concurrent_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' when q_wr_en = '1' else
            '1';

       w_foo <= I_FOO when ((I_BAR = '1') and
                (I_CRUFT = '1')) else
                '0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when q_wr_en = '1' else
                '1';

       w_foo <= I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';
    """

    def __init__(self, lTokenPairs):
        super().__init__()
        self.subphase = 2
        self.lTokenPairs = lTokenPairs
        self.configuration_documentation_link = "configuring_conditional_multiline_indent_rules_link"

        self.align_left = "no"
        self.configuration.append("align_left")
        self.align_paren = "yes"
        self.configuration.append("align_paren")
        self.wrap_at_when = "yes"
        self.configuration.append("wrap_at_when")
        self.align_when_keywords = "no"
        self.configuration.append("align_when_keywords")
        self.align_else_keywords = "no"
        self.configuration.append("align_else_keywords")

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            iFirstLine, iFirstLineIndent = alignment_utils.get_first_line_info(iLine, oFile)
            oToi.set_meta_data("iFirstLine", iFirstLine)
            oToi.set_meta_data("iFirstLineIndent", iFirstLineIndent)
            oToi.set_meta_data("iAssignColumn", oFile.get_column_of_token_index(oToi.get_start_index()))
            oToi.set_meta_data("bStartsWithParen", _starts_with_paren(lTokens))

        return lToi

    def analyze(self, oFile):
        lToi = self._get_tokens_of_interest(oFile)

        self.align_left = utils.convert_boolean_to_yes_no(self.align_left)
        self.align_paren = utils.convert_boolean_to_yes_no(self.align_paren)
        self.wrap_at_when = utils.convert_boolean_to_yes_no(self.wrap_at_when)
        self.align_when_keywords = utils.convert_boolean_to_yes_no(self.align_when_keywords)
        self.align_else_keywords = utils.convert_boolean_to_yes_no(self.align_else_keywords)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iFirstLine = oToi.get_meta_data("iFirstLine")
            iFirstLineIndent = oToi.get_meta_data("iFirstLineIndent")
            iAssignColumn = oToi.get_meta_data("iAssignColumn")
            bStartsWithParen = oToi.get_meta_data("bStartsWithParen")

            iColumn = iAssignColumn

            dActualIndent = _build_actual_indent_dict(iLine, lTokens, iFirstLineIndent)

            dIndex = _build_index_dict(iLine, lTokens)

            lActualStructure, iLastLine = _build_structure_list(iLine, iColumn, lTokens)
            lStructure = copy.deepcopy(lActualStructure)
            if iFirstLine == iLastLine:
                continue

            iFirstIndent = _find_first_indent(self.align_left, dActualIndent, self.indent_size, iAssignColumn)

            dExpectedIndent, lStructure = _apply_align_left_option(
                self.align_left,
                lStructure,
                dActualIndent,
                bStartsWithParen,
                self.indent_size,
                iAssignColumn,
                iFirstIndent,
            )
            dExpectedIndent, lStructure = _apply_align_paren_option(
                self.align_paren,
                lStructure,
                dExpectedIndent,
                bStartsWithParen,
                self.indent_size,
                iAssignColumn,
                iFirstIndent,
            )
            dExpectedIndent, lStructure = _apply_align_when_keywords_option(
                self.align_when_keywords,
                lStructure,
                dExpectedIndent,
                bStartsWithParen,
                self.indent_size,
                iAssignColumn,
                iFirstIndent,
            )
            dExpectedIndent, lStructure = _apply_align_paren_option(
                self.align_paren,
                lStructure,
                dExpectedIndent,
                bStartsWithParen,
                self.indent_size,
                iAssignColumn,
                iFirstIndent,
            )
            dExpectedIndent, lStructure = _apply_wrap_at_when_option(
                self.wrap_at_when,
                lStructure,
                dExpectedIndent,
                bStartsWithParen,
                self.indent_size,
                iAssignColumn,
                iFirstIndent,
            )
            if self.wrap_at_when == "yes" and self.align_paren == "yes":
                dExpectedIndent, lStructure = _apply_align_paren_after_when(
                    lStructure,
                    dExpectedIndent,
                    bStartsWithParen,
                    self.indent_size,
                    iAssignColumn,
                    iFirstIndent,
                )
            dExpectedIndent, lStructure = _apply_align_else_keywords_option(
                self.align_else_keywords,
                lStructure,
                dExpectedIndent,
                bStartsWithParen,
                self.indent_size,
                iAssignColumn,
                iFirstIndent,
            )

            if self.indent_style == "smart_tabs":
                alignment_utils.convert_expected_indent_to_smart_tab(dExpectedIndent, self.indent_size, iFirstLineIndent)

            for iLine in range(iFirstLine + 1, iLastLine + 1):
                if dActualIndent[iLine] == dExpectedIndent[iLine]:
                    continue

                dAction = {}
                dAction["type"] = "indent"
                dAction["line"] = iLine
                dAction["column"] = dExpectedIndent[iLine]

                if len(dActualIndent[iLine]) > 0:
                    dAction["action"] = "adjust"
                else:
                    dAction["action"] = "insert"

                sSolution = alignment_utils.build_solution(dExpectedIndent[iLine])
                iToken = dIndex[iLine]
                oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

            if self.align_when_keywords == "yes":
                for dActual, dExpect in zip(lActualStructure, lStructure):
                    if dActual["type"] == "when":
                        if dExpect["adjust"] != 0:
                            dAction = {}
                            dAction["type"] = "when"
                            dAction["line"] = dExpect["line"]
                            dAction["column"] = dExpect["column"]
                            dAction["adjust"] = dExpect["adjust"]
                            sSolution = "Align when with other whens at column " + str(dExpect["column"])
                            oViolation = violation.New(dAction["line"], oToi.extract_tokens(dActual["iToken"] - 1, dActual["iToken"] - 1), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)

            if self.align_else_keywords == "yes":
                for dActual, dExpect in zip(lActualStructure, lStructure):
                    if dActual["type"] == "else":
                        if dExpect["adjust"] != 0:
                            dAction = {}
                            dAction["type"] = "else"
                            dAction["line"] = dExpect["line"]
                            dAction["column"] = dExpect["column"]
                            dAction["adjust"] = dExpect["adjust"]
                            sSolution = "Align else with other elses at column " + str(dExpect["column"])
                            oViolation = violation.New(dAction["line"], oToi.extract_tokens(dActual["iToken"] - 1, dActual["iToken"] - 1), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction["type"] == "when":
            iSpace = len(lTokens[0].get_value())
            iNewSpace = iSpace + dAction["adjust"]
            lTokens[0].set_value(" " * iNewSpace)
        elif dAction["type"] == "else":
            iSpace = len(lTokens[0].get_value())
            iNewSpace = iSpace + dAction["adjust"]
            lTokens[0].set_value(" " * iNewSpace)
        elif dAction["type"] == "indent":
            if dAction["action"] == "adjust":
                lTokens[0].set_value(dAction["column"])
            else:
                rules_utils.insert_new_whitespace(lTokens, 0, dAction["column"])

        oViolation.set_tokens(lTokens)


def _find_first_column(oFile, oToi, sAlignLeft, iIndentSize, iIndentStep):
    iStartIndex = oToi.get_start_index()

    if sAlignLeft == "yes":
        iIndentLevel = oFile.get_indent_of_line_at_index(iStartIndex)
        iFirstColumn = iIndentLevel * iIndentSize + iIndentStep
    else:
        iFirstColumn = oFile.get_column_of_token_index(iStartIndex)

    return iFirstColumn


def is_token_before_carriage_return(tToken, lTokens):
    for oToken in lTokens:
        if isinstance(oToken, tToken):
            return True
        if isinstance(oToken, parser.carriage_return):
            return False
    return False


def _apply_align_left_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
    iFirstLine = alignment_utils.get_first_line(dActualIndent)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
    bWhenFound = False
    iParens = 0
    iLine = iFirstLine
    for dStruct in lStructure:
        if dStruct["type"] == "when":
            bWhenFound = True
        elif dStruct["type"] == "else":
            bWhenFound = False
        elif dStruct["type"] == "comma":
            bWhenFound = False
        elif dStruct["type"] == "return":
            iLine += 1
            if bWhenFound:
                if iLine == iFirstLine:
                    iIndent = iFirstIndent
                    iIndent += iIndentStep
                elif iLine == iFirstLine + 1:
                    iIndent = iFirstIndent
                    iIndent += iIndentStep
                elif len(dExpectedIndent[iLine - 1]) == iFirstIndent:
                    iIndent = iFirstIndent
                    iIndent += iIndentStep
                else:
                    iIndent = len(dExpectedIndent[iLine - 1])
                iIndent += iParens * iIndentStep
            else:
                iIndent = iFirstIndent
            dExpectedIndent[iLine] = iIndent * " "
        elif dStruct["type"] == "open":
            iParens += 1
        elif dStruct["type"] == "close":
            iParens -= 1

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_paren_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
    if sConfig == "no":
        return dActualIndent, lStructure
    iFirstLine = alignment_utils.get_first_line(dActualIndent)
    iLastLine = alignment_utils.get_last_line(dActualIndent)

    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    iIndent = iFirstIndent
    iColumn = iIndent
    lColumn = [iIndent]

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    lParens = []
    for dStruct in lStructure:
        if dStruct["type"] == "when":
            bWhenFound = True
        elif dStruct["type"] == "else":
            bWhenFound = False
        elif dStruct["type"] == "return" and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct["line"])
        elif dStruct["type"] == "open":
            iParens += 1
            lParens.append(dStruct)
        elif dStruct["type"] == "close":
            iParens -= 1
            lParens.append(dStruct)

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
        lTemp = []
        for dParen in lParens:
            if dParen["line"] == iLine:
                lTemp.append(dParen)

        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp["type"] == "open":
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp["column"] + iIndentStep - 1
                else:
                    iColumn = dTemp["column"] + (iTemp - len(dActualIndent[iLine])) + iIndentStep - 1
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn * " "
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1] * " "
                if dTemp["begin_line"]:
                    dExpectedIndent[iLine] = (len(dExpectedIndent[iLine]) - iIndentStep) * " "

        if len(lTemp) == 0:
            dExpectedIndent[iLine + 1] = lColumn[-1] * " "

        if (iLine + 1) in lWhenIndent:
            dExpectedIndent[iLine + 1] = (iFirstIndent + iIndentStep) * " "

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_when_keywords_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
    if sConfig == "no":
        return dActualIndent, lStructure

    iWhenMax = -1
    for dStruct in lStructure:
        if dStruct["type"] == "when":
            iWhenMax = max(iWhenMax, dStruct["column"])

    lNewStruct = []
    bAdjust = False
    for dStruct in lStructure:
        if dStruct["type"] == "when":
            iAdjust = iWhenMax - dStruct["column"]
            if iAdjust != 0:
                bAdjust = True
            dStruct["adjust"] = iAdjust
        if dStruct["type"] == "return":
            bAdjust = False
        if bAdjust:
            dStruct["column"] += iAdjust
        lNewStruct.append(dStruct)

    return dActualIndent, lNewStruct


def _apply_wrap_at_when_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
    if sConfig == "no":
        return dActualIndent, lStructure
    iFirstLine = alignment_utils.get_first_line(dActualIndent)
    iLastLine = alignment_utils.get_last_line(dActualIndent)

    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    bWhenFound = False
    dWhenIndent = {}
    lParens = []
    for dStruct in lStructure:
        if dStruct["type"] == "when":
            bWhenFound = True
            iColumn = dStruct["column"]
        elif dStruct["type"] == "else":
            bWhenFound = False
        elif dStruct["type"] == "return" and bWhenFound:
            dTemp = {}
            dTemp["column"] = iColumn
            dWhenIndent[dStruct["line"]] = dTemp
        elif dStruct["type"] == "open":
            lParens.append(dStruct)
        elif dStruct["type"] == "close":
            lParens.append(dStruct)

    iWhenIndent = -1
    iParens = 0

    for iLine in range(iFirstLine, iLastLine):
        lTemp = []
        for dParen in lParens:
            if dParen["line"] == iLine:
                lTemp.append(dParen)

        for dTemp in lTemp:
            if dTemp["type"] == "open":
                iParens += 1
            else:
                iParens -= 1

        if iLine + 1 in dWhenIndent:
            if iLine in dWhenIndent:
                iWhenIndent = len(dExpectedIndent[iLine]) + (iParens * iIndentStep)
            else:
                iWhenIndent = dWhenIndent[iLine + 1]["column"] + 4 + 1 + (iParens * iIndentStep)
            dExpectedIndent[iLine + 1] = iWhenIndent * " "
        else:
            dExpectedIndent[iLine + 1] = dActualIndent[iLine + 1]

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_paren_after_when(lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
    iFirstLine = alignment_utils.get_first_line(dActualIndent)
    iLastLine = alignment_utils.get_last_line(dActualIndent)

    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]

    iIndent = iFirstIndent
    lColumn = [iIndent]

    bWhenFound = False
    iParens = 0
    lWhenIndent = []
    lParens = []
    for dStruct in lStructure:
        if dStruct["type"] == "when":
            bWhenFound = True
        elif dStruct["type"] == "else":
            bWhenFound = False
        elif dStruct["type"] == "return" and bWhenFound:
            if iParens == 0:
                lWhenIndent.append(dStruct["line"])
        elif dStruct["type"] == "open":
            iParens += 1
            lParens.append(dStruct)
        elif dStruct["type"] == "close":
            iParens -= 1
            lParens.append(dStruct)

    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
        lTemp = []
        for dParen in lParens:
            if dParen["line"] == iLine:
                lTemp.append(dParen)

        iTemp = lColumn[-1]
        for dTemp in lTemp:
            if dTemp["type"] == "open":
                iParens += 1
                if iLine == iFirstLine:
                    iColumn = dTemp["column"] + iIndentStep - 1
                else:
                    iColumn = dTemp["column"] + (iTemp - len(dActualIndent[iLine])) + iIndentStep - 1
                lColumn.append(iColumn)
                dExpectedIndent[iLine + 1] = iColumn * " "
            else:
                iParens -= 1
                lColumn.pop()
                dExpectedIndent[iLine + 1] = lColumn[-1] * " "
                if dTemp["begin_line"]:
                    dExpectedIndent[iLine] = (len(dExpectedIndent[iLine]) - iIndentStep) * " "

        if len(lTemp) == 0:
            dExpectedIndent[iLine + 1] = lColumn[-1] * " "

        if (iLine + 1) in lWhenIndent and iParens == 0:
            dExpectedIndent[iLine + 1] = dActualIndent[iLine + 1]

    lReturnStructure = _update_structure(dExpectedIndent, dActualIndent, lStructure)
    return dExpectedIndent, lReturnStructure


def _apply_align_else_keywords_option(sConfig, lStructure, dActualIndent, bStartsWithParen, iIndentStep, iAssignColumn, iFirstIndent):
    if sConfig == "no":
        return dActualIndent, lStructure

    iElseMax = -1
    for dStruct in lStructure:
        if dStruct["type"] == "else":
            iElseMax = max(iElseMax, dStruct["column"])

    lNewStruct = []
    bAdjust = False
    for dStruct in lStructure:
        if dStruct["type"] == "else":
            iAdjust = iElseMax - dStruct["column"]
            if iAdjust != 0:
                bAdjust = True
            dStruct["adjust"] = iAdjust
        if dStruct["type"] == "return":
            bAdjust = False
        if bAdjust:
            dStruct["column"] += iAdjust
        lNewStruct.append(dStruct)

    return dActualIndent, lNewStruct


def _starts_with_paren(lTokens):
    iToken = utils.find_next_non_whitespace_token(1, lTokens)
    if isinstance(lTokens[iToken], parser.open_parenthesis):
        return True
    return False


def _build_actual_indent_dict(iLine, lTokens, iFirstLineIndent):
    dReturn = {}
    dReturn[iLine] = iFirstLineIndent * " "

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.blank_line):
            continue

        if isinstance(oToken, parser.carriage_return):
            dReturn[iLine] = alignment_utils.set_indent(iToken, lTokens)
            continue

    return dReturn


def _build_index_dict(iLine, lTokens):
    dReturn = {}

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.blank_line):
            continue

        if isinstance(oToken, parser.carriage_return):
            dReturn[iLine] = iToken + 1
            continue

    return dReturn


def _build_structure_list(iLine, iColumn, lTokens):
    lStructure = []

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.blank_line):
            continue

        if isinstance(oToken, parser.carriage_return):
            iColumn = 0
            dReturn = {}
            dReturn["type"] = "return"
            dReturn["line"] = iLine
            lStructure.append(dReturn)
            continue

        iColumn += len(oToken.get_value())

        if isinstance(oToken, parser.close_parenthesis):
            dParen = {}
            dParen["type"] = "close"
            dParen["line"] = iLine
            dParen["column"] = iColumn
            dParen["begin_line"] = utils.does_token_start_line(iToken, lTokens)
            lStructure.append(dParen)

        if isinstance(oToken, parser.open_parenthesis):
            dParen = {}
            dParen["type"] = "open"
            dParen["line"] = iLine
            dParen["column"] = iColumn
            lStructure.append(dParen)

        if oToken.get_lower_value() == "when":
            dWhen = {}
            dWhen["type"] = "when"
            dWhen["line"] = iLine
            dWhen["column"] = iColumn - 4
            dWhen["iToken"] = iToken
            lStructure.append(dWhen)

        if oToken.get_lower_value() == "else":
            dElse = {}
            dElse["type"] = "else"
            dElse["line"] = iLine
            dElse["column"] = iColumn - 4
            dElse["iToken"] = iToken
            lStructure.append(dElse)

        if isinstance(oToken, token.selected_waveforms.comma):
            dComma = {}
            dComma["type"] = "comma"
            dComma["line"] = iLine
            dComma["column"] = iColumn - 4
            dComma["iToken"] = iToken
            lStructure.append(dComma)

    return lStructure, iLine


def _update_structure(dExpectedIndent, dActualIndent, lStructure):
    iFirstLine = alignment_utils.get_first_line(dActualIndent)
    iLastLine = alignment_utils.get_last_line(dActualIndent)
    lReturn = []
    for iLine in range(iFirstLine, iLastLine + 1):
        iDeltaIndent = len(dExpectedIndent[iLine]) - len(dActualIndent[iLine])
        for dStruct in lStructure:
            if dStruct["line"] == iLine:
                if dStruct["type"] != "return":
                    dStruct["column"] += iDeltaIndent
                lReturn.append(dStruct)
    return lReturn


def _find_first_indent(sConfig, dActualIndent, iIndentStep, iAssignColumn):
    iFirstLine = alignment_utils.get_first_line(dActualIndent)
    if sConfig == "yes":
        iFirstIndent = len(dActualIndent[iFirstLine]) + iIndentStep
    else:
        iFirstIndent = iAssignColumn + 2 + 1
    return iFirstIndent
