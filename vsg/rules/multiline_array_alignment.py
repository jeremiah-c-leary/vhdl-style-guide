# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rule_group import alignment
from vsg.rules import alignment_utils, utils as rules_utils
from vsg.vhdlFile import utils


class multiline_array_alignment(alignment.Rule):
    """
    This rule checks the alignment of multiline constants that contain arrays.

    |configuring_multiline_indent_rules_link|

    .. NOTE:: The structure of multiline array constants is handled by the rule `constant_016 <constant_rules.html#constant-016>`_.

    **Violation**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
                0,
            65535,
            32768
         );

    **Fix**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    """

    def __init__(self, lTokenPairs):
        super().__init__()
        self.subphase = 2
        self.lTokenPairs = lTokenPairs
        self.align_left = "no"
        self.configuration.append("align_left")
        self.align_paren = "yes"
        self.configuration.append("align_paren")
        self.assignment_operator = None
        self.configuration_documentation_link = "configuring_multiline_indent_rules_link"

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            aToi = remove_non_arrays(self.assignment_operator, aToi)
            populate_toi_parameters(aToi, oFile)
            aToi = remove_single_line_assignments(aToi)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        self.align_left = utils.convert_boolean_to_yes_no(self.align_left)
        self.align_paren = utils.convert_boolean_to_yes_no(self.align_paren)

        for oToi in lToi:
            oLines = lines(oToi)
            oLines.set_first_line_indent(oToi.iFirstLineIndent)
            self.calculate_expected_indents(oToi, oLines)
            check_indents(self, oToi, oLines)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction["action"] == "adjust":
            lTokens[0].set_value(dAction["whitespace"])
        else:
            rules_utils.insert_new_whitespace(lTokens, 0, dAction["whitespace"])

        oViolation.set_tokens(lTokens)

    def calculate_expected_indents(self, oToi, oLines):
        dExpectedIndent = {}
        if not align_paren(self) and align_left(self):
            dExpectedIndent = self.analyze_align_left_true_align_paren_false(oToi, oLines)
        if align_paren(self) and not align_left(self):
            dExpectedIndent = self.analyze_align_left_false_align_paren_true(oToi, oLines)
        if align_paren(self) and align_left(self):
            dExpectedIndent = self.analyze_align_left_true_align_paren_true(oToi, oLines)

        return dExpectedIndent

    def analyze_align_left_true_align_paren_false(self, oToi, oLines):
        oLines.iIndent = oLines.get_first_line_indent()
        oLines.iParens = 0
        oLines.indent_size = self.indent_size
        for oLine in oLines.lLines:
            if oLine.isFirst:
                oLines.set_first_line_expected_indent(oLines.iIndent)
            else:
                check_left_aligned_line(oLine, oLines)

            oLines.iParens += oLine.get_delta_parens()

    def analyze_align_left_false_align_paren_true(self, oToi, oLines):
        for oLine in oLines.lLines:
            if oLine.isFirst:
                check_first_line(oLine, oLines, oToi, self.indent_size)
            elif oLine.isLast:
                check_last_line(oLine, oLines, self.indent_size)
            else:
                check_middle_line(oLine, oLines, self.indent_size)

    def analyze_align_left_true_align_paren_true(self, oToi, oLines):
        for oLine in oLines.lLines:
            if oLine.isFirst:
                check_my_first_line(oLine, oLines, oToi, self.indent_size)
            elif oLine.isLast:
                check_last_line(oLine, oLines, self.indent_size)
            else:
                check_middle_line(oLine, oLines, self.indent_size)


def _set_indent(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        iReturn = len(lTokens[iToken + 1].get_value())
    else:
        iReturn = 0
    return iReturn


def check_left_aligned_line(oLine, oLines):
    if rules_utils.token_list_begins_with_close_paren(oLine.tokens):
        oLine.set_expected_indent(oLines.iIndent + oLines.iParens * oLines.indent_size - oLines.indent_size)
    else:
        oLine.set_expected_indent(oLines.iIndent + oLines.iParens * oLines.indent_size)


def check_first_line(oLine, oLines, oToi, iIndentStep):
    iIndent = oLines.get_first_line_indent()
    oLine.set_expected_indent(iIndent)

    iAdjust = oToi.iAssignColumn
    oLines.update_parens(oLine, iIndentStep, iAdjust)

    if oLines.no_parens():
        oLines.iNextIndent = iIndent
    else:
        oLines.iNextIndent = oLines.lParens[-1].iExpectedColumn


def check_last_line(oLine, oLines, iIndentStep):
    set_expected_indent_of_line(oLine, oLines, iIndentStep)
    oLines.update_parens(oLine, iIndentStep)


def check_middle_line(oLine, oLines, iIndentStep):
    set_expected_indent_of_line(oLine, oLines, iIndentStep)
    oLines.update_parens(oLine, iIndentStep)
    if not oLines.no_parens():
        oLines.iNextIndent = oLines.lParens[-1].iExpectedColumn


def set_expected_indent_of_line(oLine, oLines, iIndentStep):
    if oLine.starts_with_close_paren():
        oLine.set_expected_indent(oLines.iNextIndent - iIndentStep)
    else:
        oLine.set_expected_indent(oLines.iNextIndent)


def check_my_first_line(oLine, oLines, oToi, iIndentStep):
    iIndent = oLines.get_first_line_indent()
    oLine.set_expected_indent(iIndent)

    iAdjust = oToi.iAssignColumn
    oLines.update_parens(oLine, iIndentStep, iAdjust)

    if oLines.no_parens():
        oLines.iNextIndent = iIndent
    else:
        oLines.iNextIndent = len(oLines.lParens) * iIndentStep + iIndent

    for iParen, oParen in enumerate(oLine.parens):
        oParen.iExpectedColumn = iParen * iIndentStep + iIndent + iIndentStep


def remove_non_arrays(assignment_operator, lToi):
    lReturn = []
    for oToi in lToi:
        if rules_utils.array_detected_after_assignment_operator(assignment_operator, oToi):
            lReturn.append(oToi)
    return lReturn


def remove_single_line_assignments(lToi):
    lReturn = []
    for oToi in lToi:
        if oToi.iFirstLine != oToi.iLastLine:
            lReturn.append(oToi)
    return lReturn


def set_last_line_number(oToi):
    iLine, lTokens = utils.get_toi_parameters(oToi)
    for oToken in lTokens:
        iLine = utils.increment_line_number(iLine, oToken)

    oToi.iLastLine = iLine


def populate_toi_parameters(aToi, oFile):
    for oToi in aToi:
        oToi.iFirstLine = oToi.iLine
        lTemp = oFile.get_tokens_from_line(oToi.iLine)
        iIndent = len(lTemp.get_tokens()[0].get_value())
        oToi.iFirstLineIndent = iIndent

        oToi.iFirstLineIndentIndex = oFile.get_indent_of_line_at_index(oToi.get_start_index())

        oToi.iAssignColumn = oFile.get_column_of_token_index(oToi.get_start_index())
        set_last_line_number(oToi)


def check_indents(self, oToi, oLines):
    for oLine in oLines.lLines[1:]:
        if oLine.isBlank:
            continue
        sExpectedIndent = convert_column_index_to_whitespace(self, oLine.get_expected_indent(), oLines.get_first_line_indent(), oToi.iFirstLineIndentIndex)
        oLine.sExpectedIndent = sExpectedIndent
        if sExpectedIndent != oLine.actual_leading_whitespace:
            oViolation = create_violation(oToi, oLine)
            self.add_violation(oViolation)


def convert_column_index_to_whitespace(self, iColumn, iFirstLineIndent, iFirstLineIndentIndex):
    if self.indent_style == "smart_tabs":
        sIndent = "\t" * iFirstLineIndentIndex
        sAlignment = " " * (iColumn - iFirstLineIndent)
    else:
        sIndent = " " * self.indent_size * iFirstLineIndentIndex
        sAlignment = " " * (iColumn - len(sIndent))
    sLeadingWhitespace = sIndent + sAlignment
    return sLeadingWhitespace


def create_violation(oToi, oLine):
    iToken = oLine.token_index
    iLine = oLine.number
    lTokens = oToi.extract_tokens(iToken, iToken)
    sSolution = alignment_utils.build_solution(oLine.sExpectedIndent)

    oViolation = violation.New(iLine, lTokens, sSolution)
    oViolation.set_action(create_action_dict(oLine))

    return oViolation


def create_action_dict(oLine):
    dAction = {}
    dAction["line"] = oLine.number
    dAction["column"] = oLine.iExpectedIndent
    dAction["whitespace"] = oLine.sExpectedIndent

    if isinstance(oLine.tokens[0], parser.whitespace):
        dAction["action"] = "adjust"
    else:
        dAction["action"] = "insert"
    return dAction


class lines:
    def __init__(self, oToi):
        self.oToi = oToi
        self.lParens = []
        self.lLines = []
        self._convert_toi(oToi)

    def _convert_toi(self, oToi):
        iLine, lTokens = utils.get_toi_parameters(oToi)
        lLine = []
        bFirstLine = True
        iOffset = 0
        for iToken, oToken in enumerate(lTokens):
            lLine.append(oToken)
            if rules_utils.token_is_carriage_return(oToken):
                oLine = line(lLine, iLine, iToken - len(lLine) + 1, iOffset)
                oLine.isFirst = bFirstLine
                bFirstLine = False
                if isinstance(lTokens[iToken - 1], parser.blank_line):
                    oLine.isBlank = True
                self.lLines.append(oLine)
                iLine += 1
                iOffset = 0
                lLine = []

        oLine = line(lLine, iLine, iToken - len(lLine) + 1)
        oLine.isLast = True
        self.lLines.append(oLine)

    def set_first_line_indent(self, iIndent):
        self.lLines[0].actual_indent = iIndent

    def get_first_line_indent(self):
        return self.lLines[0].actual_indent

    def set_first_line_expected_indent(self, iIndent):
        self.lLines[0].set_expected_indent(iIndent)

    def no_parens(self):
        if len(self.lParens) == 0:
            return True
        return False

    def update_parens(self, oLine, iIndentStep, iAdjust=0):
        self.lParens = oLine.update_parens(self.lParens, iIndentStep, iAdjust)


class line:
    def __init__(self, lLine, iLine, iToken, iIndent=0):
        self.number = iLine
        self.tokens = lLine
        self.parens = []
        self.populate_paren_list(iIndent)
        self.set_actual_indent()
        self.set_actual_leading_whitespace()
        self.token_index = iToken
        self.isFirst = False
        self.isLast = False
        self.iExpectedIndent = 0
        self.isBlank = False

    def populate_paren_list(self, iIndent):
        iColumn = iIndent
        for oToken in self.tokens:
            iColumn += len(oToken.get_value())
            if rules_utils.token_is_open_paren(oToken):
                oParen = paren("open", iColumn)
                self.parens.append(oParen)
            if rules_utils.token_is_close_paren(oToken):
                oParen = paren("close", iColumn)
                self.parens.append(oParen)

    def set_actual_indent(self):
        oToken = self.tokens[0]
        self.actual_indent = 0
        if rules_utils.token_is_whitespace(oToken):
            self.actual_indent = len(oToken.get_value())

    def set_actual_leading_whitespace(self):
        oToken = self.tokens[0]
        self.actual_leading_whitespace = ""
        if rules_utils.token_is_whitespace(oToken):
            self.actual_leading_whitespace = oToken.get_value()

    def get_delta_parens(self):
        iReturn = 0
        for oParen in self.parens:
            if oParen.is_open():
                iReturn += 1
            else:
                iReturn -= 1
        return iReturn

    def set_expected_indent(self, iIndent):
        self.iExpectedIndent = iIndent

    def get_expected_indent(self):
        return self.iExpectedIndent

    def starts_with_close_paren(self):
        return rules_utils.token_list_begins_with_close_paren(self.tokens)

    def update_parens(self, lParens, iIndentStep, iAdjust=0):
        update_parens_expected_column(self, iIndentStep, iAdjust)
        lParens.extend(self.parens)
        lReturn = remove_matching_parens(lParens)
        return lReturn


def update_parens_expected_column(self, iIndentStep, iAdjust=0):
    for oParen in self.parens:
        oParen.iExpectedColumn = oParen.iColumn + iAdjust - self.actual_indent + self.iExpectedIndent + iIndentStep - 1


def remove_matching_parens(lParens):
    lReturn = []
    for oParen in lParens:
        if oParen.is_open():
            lReturn.append(oParen)
        if oParen.is_close():
            lReturn.pop()
    return lReturn


class paren:
    def __init__(self, sType, iColumn, iId=None):
        self.sType = sType
        self.iColumn = iColumn
        self.iId = iId
        self.iExpectedColumn = iColumn

    def is_open(self):
        if self.sType == "open":
            return True
        return False

    def is_close(self):
        if self.sType == "close":
            return True
        return False


def align_left(self):
    if self.align_left == "yes":
        return True
    return False


def align_paren(self):
    if self.align_paren == "yes":
        return True
    return False
