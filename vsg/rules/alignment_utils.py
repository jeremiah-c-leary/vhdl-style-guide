
from vsg import parser
from vsg import token

from vsg.vhdlFile import utils


def build_solution(sIndent):
    sSolution = 'Indent with '
    if '\t' in sIndent and ' ' in sIndent:
        sSolution += str(sIndent.count('\t')) + ' tab(s) followed by ' + str(sIndent.count(' ')) + ' space(s)'
    elif '\t' in sIndent:
        sSolution += str(sIndent.count('\t')) + ' tab(s)'
    elif ' ' in sIndent:
        sSolution += str(sIndent.count(' ')) + ' space(s)'
    return sSolution


def convert_expected_indent_to_smart_tab(dExpectedIndent, indentSize, iFirstLineIndent):
    iFirstLine = get_first_line(dExpectedIndent)
    iLastLine = get_last_line(dExpectedIndent)
    for iLine in range(iFirstLine + 1, iLastLine + 1):
        dExpectedIndent[iLine] = '\t' + dExpectedIndent[iLine][iFirstLineIndent:]


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
        iReturn = ''
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
        iTabs = sToken.count('\t')
        iLength = len(sToken) + (iTabs * self.indentSize) - iTabs
        return iLength

    return len(oToken.get_value())


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment, include_lines_without_comments=False, iMaxColumn=0):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['left_column'])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]['left_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['token_column'])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]['token_column'])

    if include_lines_without_comments:
        iMaxTokenColumn = max(iMaxTokenColumn, iMaxColumn)

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['token_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['token_column']


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
