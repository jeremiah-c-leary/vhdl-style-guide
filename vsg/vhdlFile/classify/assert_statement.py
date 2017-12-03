import re


def assert_statement(dVars, oLine):

    if re.match('^\s*assert', oLine.line, re.IGNORECASE):
        oLine.isAssertKeyword = True
        oLine.insideAssert = True
    if oLine.insideAssert:
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    if oLine.insideAssert and ';' in oLine.line:
        oLine.isAssertEnd = True
