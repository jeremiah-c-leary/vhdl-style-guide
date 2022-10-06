
from vsg import parser
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
