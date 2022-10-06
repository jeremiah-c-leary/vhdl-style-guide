
from vsg import parser


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
