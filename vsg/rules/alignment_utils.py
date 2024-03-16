# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


def build_solution(sIndent):
    sSolution = "Indent with "
    if "\t" in sIndent and " " in sIndent:
        sSolution += str(sIndent.count("\t")) + " tab(s) followed by " + str(sIndent.count(" ")) + " space(s)"
    elif "\t" in sIndent:
        sSolution += str(sIndent.count("\t")) + " tab(s)"
    elif " " in sIndent:
        sSolution += str(sIndent.count(" ")) + " space(s)"
    return sSolution


def convert_expected_indent_to_smart_tab(dExpectedIndent, indent_size, iFirstLineIndent):
    iFirstLine = get_first_line(dExpectedIndent)
    iLastLine = get_last_line(dExpectedIndent)
    for iLine in range(iFirstLine + 1, iLastLine + 1):
        dExpectedIndent[iLine] = "\t" + dExpectedIndent[iLine][iFirstLineIndent:]


def get_first_line(dActualIndent):
    lLines = list(dActualIndent.keys())
    lLines.sort()
    iLine = lLines[0]
    return iLine


def get_first_line_info(iLine, oFile):
    lTemp = oFile.get_tokens_from_line(iLine)
    iIndent = len(lTemp.get_tokens()[0].get_value())
    return iLine, iIndent


def get_last_line(dActualIndent):
    lLines = list(dActualIndent.keys())
    lLines.sort()
    iLine = lLines[-1]
    return iLine


def set_indent(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        iReturn = lTokens[iToken + 1].get_value()
    else:
        iReturn = ""
    return iReturn


def starts_with_paren(lTokens):
    iToken = utils.find_next_non_whitespace_token(1, lTokens)
    try:
        if isinstance(lTokens[iToken], parser.open_parenthesis):
            return True
    except IndexError:
        if isinstance(lTokens[0], parser.open_parenthesis):
            return True
    return False


def update_column_width(self, oToken):
    sToken = oToken.get_value()
    if isinstance(oToken, parser.whitespace):
        iTabs = sToken.count("\t")
        iLength = len(sToken) + (iTabs * self.indent_size) - iTabs
        return iLength

    return len(oToken.get_value())


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment, include_lines_without_comments=False, iMaxColumn=0):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]["left_column"])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]["left_column"])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]["token_column"])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]["token_column"])

    if include_lines_without_comments:
        iMaxTokenColumn = max(iMaxTokenColumn, iMaxColumn)

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]["adjust"] = iMaxLeftColumn - dAnalysis[iKey]["token_column"] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]["adjust"] = iMaxTokenColumn - dAnalysis[iKey]["token_column"]


def check_for_exclusions(oToken, bSkip, oEndSkipToken, lUnless):
    if bSkip:
        if isinstance(oToken, oEndSkipToken):
            return False, None
    else:
        for lTokenPairs in lUnless:
            if isinstance(oToken, lTokenPairs[0]):
                return True, lTokenPairs[1]

    return bSkip, oEndSkipToken


def check_for_if_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.if_statement.if_label):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.if_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.elsif_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.else_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.if_statement.end_keyword):
        return True

    return False


def check_for_case_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.case_statement.case_label):
        return True

    if isinstance(lTokens[iMyToken], token.case_statement.case_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.case_statement.end_keyword):
        return True

    return False


def check_for_when_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.case_statement_alternative.when_keyword):
        return True

    return False


def check_for_loop_keywords(iToken, lTokens):
    iMyToken = iToken
    if isinstance(lTokens[iToken], parser.whitespace):
        iMyToken += 1

    if isinstance(lTokens[iMyToken], token.loop_statement.loop_label):
        return True

    if isinstance(lTokens[iMyToken], token.iteration_scheme.while_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.iteration_scheme.for_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.loop_statement.loop_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.loop_statement.end_keyword):
        return True

    if isinstance(lTokens[iMyToken], token.loop_statement.end_loop_keyword):
        return True

    return False


def check_for_aggregate_parens(iToken, lTokens):
    iMyToken = iToken

    if isinstance(lTokens[iMyToken], token.aggregate.open_parenthesis):
        return True

    if isinstance(lTokens[iMyToken], token.aggregate.close_parenthesis):
        return True

    return False


def is_single_line_aggregate(iToken, lTokens):
    if not isinstance(lTokens[iToken], token.aggregate.open_parenthesis):
        return False

    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.carriage_return):
            return False
        if isinstance(lTokens[iIndex], token.aggregate.close_parenthesis):
            if lTokens[iIndex].iId == lTokens[iToken].iId:
                return True
    return False


def check_for_violations(self, dAnalysis, oFile):
    add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
    for iKey in list(dAnalysis.keys()):
        if dAnalysis[iKey]["adjust"] != 0:
            oLineTokens = oFile.get_tokens_from_line(iKey)
            sSolution = "Move " + dAnalysis[iKey]["token_value"] + " " + str(dAnalysis[iKey]["adjust"]) + " columns"
            oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
            oViolation.set_action(dAnalysis[iKey])
            self.add_violation(oViolation)


def generate_statement_detected(self, oToken):
    if not self.generate_statement_ends_group:
        return False
    if generate_label_detected(oToken):
        return True
    if generate_semicolon_detected(oToken):
        return True
    if case_generate_alternative_detected(oToken):
        return True
    return False


def generate_label_detected(oToken):
    if isinstance(oToken, token.if_generate_statement.generate_label):
        return True
    if isinstance(oToken, token.for_generate_statement.generate_label):
        return True
    return False


def generate_semicolon_detected(oToken):
    if isinstance(oToken, token.if_generate_statement.semicolon):
        return True
    if isinstance(oToken, token.for_generate_statement.semicolon):
        return True
    if isinstance(oToken, token.case_generate_statement.semicolon):
        return True
    return False


def case_generate_alternative_detected(oToken):
    if isinstance(oToken, token.case_generate_alternative.when_keyword):
        return True
    return False


def is_case_control_enabled(config):
    if config == "break_on_case_or_end_case":
        return True
    return config


def is_case_keyword(config, iIndex, lTokens):
    if check_for_case_keywords(iIndex + 1, lTokens):
        return True
    if check_for_when_keywords(iIndex + 1, lTokens):
        if config != "break_on_case_or_end_case":
            return True
    return False


def unless_region_detected(oToken, lUnless):
    for lTokenPairs in lUnless:
        if isinstance(oToken, lTokenPairs[0]):
            return True
    return False


def get_index_of_end_unless_region(oToken, lTokens, lUnless, iIndex):
    for lTokenPairs in lUnless:
        if isinstance(oToken, lTokenPairs[0]):
            return rules_utils.get_index_of_token_in_list_after_index(lTokenPairs[1], lTokens, iIndex)
